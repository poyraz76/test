metadata = """
summary @ C++ bindings for pango
homepage @ http://gtkmm.sourceforge.net/
license @ LGPL
src_url @ http://ftp.gnome.org/pub/GNOME/sources/$name/2.36/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ media-libs/pango dev-cpp/glibmm dev-cpp/cairomm
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
