from nnverify import config
from nnverify.analyzer import Analyzer
from nnverify.common.result import Result, Results
from nnverify.proof_transfer.pt_util import compute_speedup, plot_verification_results
from nnverify.proof_transfer.pt_types import ProofTransferMethod
from nnverify.common.dataset import Dataset


class TransferArgs:
    def __init__(self, domain, approx, pt_method=None, count=None, eps=0.01, dataset='mnist', attack='linf',
                 split=None, net='',
                 timeout=30):
        self.net = config.NET_HOME + net
        self.domain = domain
        self.pt_method = pt_method
        self.count = count
        self.eps = eps
        self.dataset = dataset
        self.attack = attack
        self.split = split
        self.approximation = approx
        self.timeout = timeout

    def set_net(self, net):
        self.net = config.NET_HOME + net

    def get_verification_arg(self):
        arg = config.Args(net=self.net, domain=self.domain, dataset=self.dataset, eps=self.eps,
                          split=self.split, count=self.count, pt_method=self.pt_method, timeout=self.timeout)
        # net is set correctly again since the home dir is added here
        arg.net = self.net
        return arg


def proof_transfer(pt_args):
    res, res_pt = proof_transfer_analyze(pt_args)

    speedup = compute_speedup(res, res_pt, pt_args)
    print("Proof Transfer Speedup :", speedup)
    plot_verification_results(res, res_pt, pt_args)
    return speedup


def proof_transfer_acas(pt_args):
    res = Results(pt_args)
    res_pt = Results(pt_args)
    for i in range(1, 6):
        for j in range(1, 10):
            pt_args.set_net(config.ACASXU(i, j))
            pt_args.count = 4
            r, rp = proof_transfer_analyze(pt_args)
            res.results_list += r.results_list
            res_pt.results_list += rp.results_list

    # compute merged stats
    res.compute_stats()
    res_pt.compute_stats()

    speedup = compute_speedup(res, res_pt, pt_args)
    print("Proof Transfer Speedup :", speedup)
    plot_verification_results(res, res_pt, pt_args)
    return speedup

def proof_transfer_AAAI(pt_args):
    res = Results(pt_args)
    res_pt = Results(pt_args)
    
    
    for data in [\
                    34, 35]:
    # for data in [1, 2, 3, 4, 5, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,  31, 33, ]:
        # for perturb_rate in [0.001, 0.01, 0.03, 0.05]:
        for perturb_rate in [0.001]:
            if data == 1 and perturb_rate == 0.001:
                continue
            pt_args.count = data
            # pt_args.set_net(config.ACASXU_randomized_torch(random=perturb_rate))
            pt_args.set_net(config.ACASXU(5, 2))
            r, rp = proof_transfer_analyze_aaai(pt_args,perturb_rate)
            if (r is None) and (rp is None):
                print('first verify is timeout !!!')
                continue 
            res.results_list += r.results_list
            res_pt.results_list += rp.results_list

    # compute merged stats
            res.compute_stats_AAAI()
            res_pt.compute_stats_AAAI()
            print('completed !!!')

            speedup = compute_speedup(res, res_pt, pt_args)
            print("Proof Transfer Speedup :", speedup)
            plot_verification_results(res, res_pt, pt_args)
    # return speedup


def proof_transfer_analyze(pt_args):
    args = pt_args.get_verification_arg()
    print("Running IVAN on the original network")
    analyzer = Analyzer(args)
    _ = analyzer.run_analyzer()
    template_store = analyzer.template_store
    if args.pt_method == ProofTransferMethod.ALL:
        # precomputes reordered template store
        template_store = get_reordered_template_store(args, template_store)
    approx_net = get_perturbed_network(pt_args)
    # Use template generated from original verification for faster verification of the approximate network
    approx_args = pt_args.get_verification_arg()
    print("Running IVAN on updated network")
    res_pt = Analyzer(approx_args, net=approx_net, template_store=template_store).run_analyzer()
    # Compute results without any template store as the baseline
    print("Running the baseline on the updated network")
    res = Analyzer(args, net=approx_net).run_analyzer()
    return res, res_pt

def proof_transfer_analyze_aaai(pt_args, perturb_rate):
    args = pt_args.get_verification_arg()
    print("Running IVAN on the original network")
    analyzer = Analyzer(args)
    _, is_timeout = analyzer.run_analyzer()
    if is_timeout:
        return None, None
    template_store = analyzer.template_store
    if args.pt_method == ProofTransferMethod.ALL:
        # precomputes reordered template store
        template_store = get_reordered_template_store(args, template_store)
    # start incremental verification
    if pt_args.dataset == Dataset.AAAI:
        pt_args.set_net(config.ACASXU_randomized_torch(random=perturb_rate))
    approx_net = get_perturbed_network(pt_args)
    # Use template generated from original verification for faster verification of the approximate network
    approx_args = pt_args.get_verification_arg()
    print("Running IVAN on updated network")
    res_pt,_ = Analyzer(approx_args, net=approx_net, template_store=template_store).run_analyzer()
    # Compute results without any template store as the baseline
    print("Running the baseline on the updated network")
    res,_ = Analyzer(args, net=approx_net).run_analyzer()
    return res, res_pt


def get_reordered_template_store(args, template_store):
    args.pt_method = ProofTransferMethod.REORDERING
    # Compute reordered template
    analyzer_reordering = Analyzer(args, template_store=template_store)
    # TODO: make this as a separate a function from run_analyzer that takes some budget for computing
    _ = analyzer_reordering.run_analyzer()
    # This template store should contain leaf nodes of reordered tree
    template_store = analyzer_reordering.template_store
    return template_store


def get_perturbed_network(pt_args):
    # Generate the approximate network
    approx_net = pt_args.approximation.approximate(pt_args.net, pt_args.dataset)   
    return approx_net
