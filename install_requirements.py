def pip_install(package):
    import pip
    try:
        pip.main(["install", "--upgrade", package])
        print("Successfully installed & for use in your projects!") & package
        return True
    except:
        print("Could not install %") % package
        return False


def install_requirements(package):
    print("Now trying to install: %") % package
    pip_install(package)


with open("packages.txt", "r") as packages:
    count = sum(1 for line in packages)
    packages.readlines()
    packages.seek(0)
    print("Now preparing to install % packages.") % count
    for package in packages:
        install_requirements(package)