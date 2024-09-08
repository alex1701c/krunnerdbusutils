### krunnerdbusutils

Utilities for writing a KRunner plugin using python.

Usage example:

```py
from krunnerdbusutils import krunner_actions, krunner_match, krunner_run, \
    AbstractRunner, Action, Match, run_event_loop


class Runner(AbstractRunner):
    def __init__(self):
        super().__init__("net.fancyplugin2", "/fancyplugin")

    @krunner_match
    def Match(self, query: str):
        matches = []
        if query == "hello":
            match = Match() # Or utilize keyword constructor
            match.id = "hello_match"
            match.text = "Hello There!"
            match.subtext = "Example"
            match.icon = "planetkde"
            matches.append(match)
        return matches

    @krunner_actions
    def Actions(self):
        return [Action(id="id", text="Action Tooltip", icon="planetkde")]

    @krunner_run
    def Run(self, data: str, action_id: str):
        print(data, action_id)


if __name__ == "__main__":
    run_event_loop(Runner)
```
