metadata = """
summary @ X.org framebuffer video driver
homepage @ http://xorg.freedesktop.org/
license @ GPL
src_url @ http://xorg.freedesktop.org/archive/individual/driver/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
build @ x11-proto/dri2proto
"""
def configure():
    export("HOME", build_dir)
    conf()

def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)

