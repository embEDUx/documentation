# FAQ
This should one day be realized as a standalone bugtracker.

# RootFS
## Package Specific Problems
### *net-wireless/gnuradio* - fails on armv6\_hardfp due to lack of NEON support
This was first encountered with package during the RootFS buildjob on the armv6j\_hardfp buildslave.

#### Build Log Snippet
```
libvolk.so.0.0.0: undefined reference to `volk_16i_max_star_horizontal_16i_neonasm'
libvolk.so.0.0.0: undefined reference to `volk_32fc_x2_multiply_32fc_neonasm'
libvolk.so.0.0.0: undefined reference to `volk_32fc_32f_dot_prod_32fc_a_neonasm'
libvolk.so.0.0.0: undefined reference to `volk_32f_x2_dot_prod_32f_neonasm'
libvolk.so.0.0.0: undefined reference to `volk_32f_x2_dot_prod_32f_neonasm_opts'
libvolk.so.0.0.0: undefined reference to `volk_32fc_32f_dot_prod_32fc_a_neonpipeline'
collect2: error: ld returned 1 exit status
volk/lib/CMakeFiles/test_all.dir/build.make:119: recipe for target 'volk/lib/test_all' failed
make[2]: *** [volk/lib/test_all] Error 1
make[2]: Leaving directory '/var/tmp/portage/net-wireless/gnuradio-3.7.6/work/gnuradio-3.7.6_build'
CMakeFiles/Makefile2:132: recipe for target 'volk/lib/CMakeFiles/test_all.dir/all' failed
make[1]: *** [volk/lib/CMakeFiles/test_all.dir/all] Error 2
make[1]: Leaving directory '/var/tmp/portage/net-wireless/gnuradio-3.7.6/work/gnuradio-3.7.6_build'
Makefile:146: recipe for target 'all' failed
make: *** [all] Error 2
 * ERROR: net-wireless/gnuradio-3.7.6::gentoo failed (compile phase):
 *   emake failed
 * 
 * If you need support, post the output of `emerge --info '=net-wireless/gnuradio-3.7.6::gentoo'`,
 * the complete build log and the output of `emerge -pqv '=net-wireless/gnuradio-3.7.6::gentoo'`.
 * The complete build log is located at '/var/tmp/portage/net-wireless/gnuradio-3.7.6/temp/build.log'.
 * The ebuild environment file is located at '/var/tmp/portage/net-wireless/gnuradio-3.7.6/temp/environment'.
 * Working directory: '/var/tmp/portage/net-wireless/gnuradio-3.7.6/work/gnuradio-3.7.6_build'
 * S: '/var/tmp/portage/net-wireless/gnuradio-3.7.6/work/gnuradio-3.7.6'
```

#### Solution
* Upstream bug ticket: https://gnuradio.org/redmine/issues/692
**(work in progress)**
