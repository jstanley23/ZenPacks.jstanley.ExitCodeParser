from Products.ZenRRD.CommandParser import CommandParser


class ExitCode(CommandParser):
    def processResults(self, cmd, result):
        output = cmd.result.output

        exitCode = cmd.result.exitCode
        if exitCode > 5:
            exitCode = 5
        elif exitCode < 0:
            exitCode = 0

        result.events.append(
            dict(
                summary=output,
                message=output,
                component=cmd.component,
                eventKey=cmd.eventKey,
                eventClass=cmd.eventClass,
                severity=exitCode,
            )
        )

    @property
    def createDefaultEventUsingExitCode(self):
        return False