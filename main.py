from system import SistemaPrincipal

def main():
    sys = SistemaPrincipal()
    core = True
    while core:
        core = sys.menuUser()
    pass


if __name__ == '__main__':
    main()