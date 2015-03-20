# Evaluation
The [design considerations](design.md) will be evaluated within this chapter.

First the already existing solutions are evaluated.

* [Yocto Project](evaluation/yocto-project.md)
* [Buildroot](evaluation/buildroot.md) 

At the time of writing this evaluation, the evaluation of these two solutions
was already made and therefore also the decision against them. The following
evaluations are based on the decision to implement **embEDUx** as a new build
system solution.

Please select a topic of interest. 

* [Buildserver Setuproutine](evaluation/buildserver-setuproutine.md)
* [Container Utility](evaluation/container-utility.md)
* [Continuous Integration](evaluation/continuous-integration.md)
* [Flashtool](evaluation/flashtool.md)
* [Linux-Kernel](evaluation/linux.md)
* [RootFS](evaluation/rootfs.md)
* [Toolchain](evaluation/toolchain.md)
* [U-Boot](evaluation/uboot.md)

# Post-Evaluation System Overall Design
These is the design which resulted from the evaluation process. For a better
understanding the **embEDUx** buildserver side and the **Flashtool** side are
divided into two images.

## Buildserver
[![](background/img/post-eval_result_design.png)](background/img/post-eval_result_design.png)

## Flashtool
[![](background/img/post-eval_result_design_flashtool.png)](background/img/post-eval_result_design_flashtool.png)

