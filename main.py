
from ultralytics.scripts.destroyerPickaxe import DestroyerPickAxe
from ultralytics.scripts.base import BaseScript
from ultralytics.scripts.domination import Domination
from ultralytics.scripts.attackspam import AttackSpam
from ultralytics.scripts.attacker import Attacker


class MortalScripts(BaseScript):

    def __init__(self):
        super().__init__()

        # Подключенные скрипты
        self.scripts_pack = {
            Domination(),
            AttackSpam(),
            Attacker(),
            # Spacer(),
            # MentalTraining(),
            DestroyerPickAxe(),
        }

    def run(self):
        while not self.exitKey:
            for script in self.scripts_pack:
                script.run()
            self.checkExitKey()
            self.wait(0.01)


def run():
    mortal_script = MortalScripts()
    mortal_script.run()


if __name__ == "__main__":
    run()
