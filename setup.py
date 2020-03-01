from distutils.core import setup, Extension

SOURCES = []

module = Extension("beegen", sources = SOURCES)

setup(
    name="Beegen",
    version="001",
    description="ssh-beegen -t rsa -b movie",
    ext_modules=[module]
)
