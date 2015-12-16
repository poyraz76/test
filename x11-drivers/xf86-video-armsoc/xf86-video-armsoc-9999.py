metadata = """
summary @  ARMSoC Mali FrameBuffer driver for ODROID
homepage @ https://github.com/mdrjr/xf86-video-armsoc/tree/r4p0
license @ GPL2
arch @ ~x86_64
"""

depends = """
build @ x11-proto/dri2proto
"""
standard_procedure = False

get("python_utils", "git_utils")

def prepare():
    git_clone("git://github.com/mdrjr/xf86-video-armsoc.git", subdir=name)
    
    
def configure():
    cd("xf86-video-armsoc")
    system("./autogen.sh --prefix=/usr --with-drmmode=exynos")

def build():
    cd("xf86-video-armsoc")
    make()

def install():
    cd("xf86-video-armsoc")
    raw_install("DESTDIR=%s" % install_dir)

