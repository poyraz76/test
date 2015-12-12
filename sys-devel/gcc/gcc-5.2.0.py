metadata = """
summary @ The GNU Compiler Collection
homepage @ http://gcc.gnu.org/
license @ GPL-3 LGPL-3
src_url @ ftp://gcc.gnu.org/pub/gcc/releases/$fullname/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
common @ sys-devel/binutils dev-libs/mpc >=sys-libs/zlib-1.1.4 >=dev-libs/mpfr-2.4.2
#build @ >=sys-apps/texinfo-4.8 >=sys-devel/bison-1.875 >=sys-devel/flex-2.5.4
"""

def prepare():
    del_cflags("-pipe")
    del_cxxflags("-pipe")
  
def configure():
    sed("-i 's@\./fixinc\.sh@-c true@' gcc/Makefile.in")
    
    sed("-i '/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/' {libiberty,gcc}/configure")
    
    makedirs("../gcc-build"); cd("../gcc-build")
    del_cflags("-pipe")
    del_cxxflags("-pipe")
    conf("--libdir=/usr/lib --libexecdir=/usr/lib \
      --mandir=/usr/share/man --infodir=/usr/share/info \
      --enable-languages=c,c++\
      --enable-shared --enable-threads=posix \
      --with-system-zlib --enable-__cxa_atexit \
      --disable-libunwind-exceptions --enable-clocale=gnu \
      --disable-libstdcxx-pch --disable-libssp \
      --enable-gnu-unique-object --enable-linker-build-id \
      --enable-lto --enable-plugin --enable-install-libiberty \
      --with-linker-hash-style=gnu --enable-gnu-indirect-function \
      --disable-multilib --disable-werror \
      --enable-checking=release \
      --with-arch=armv7-a --with-float=hard --with-fpu=vfpv3-d16",run_dir=build_dir)
    

def build():
    cd("../gcc-build")
   # make()
    make()

def install():
    cd("../gcc-build")
    # install gcc
    raw_install("DESTDIR=%s" % install_dir)
    # create symlinks
    makesym("/usr/bin/gcc" , "/usr/bin/cc")
    makesym("/usr/bin/cpp" , "/lib/cpp")
