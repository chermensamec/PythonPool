'''Class which imitate of key of console'''
class PassCraker:
    '''Class which imitate of key of console'''
    def __init__(self) -> None:
        self.passphrase = 'zax2rulez'

    def __str__(self) -> str:
        return 'GeneralTsoKeycard'

    def __gt__(self, other) -> str:
        return other > 9000

    def __len__(self) -> int:
        return 1337

    def __getitem__(self, key) -> int:
        if key == 404:
            return 4
        return 916