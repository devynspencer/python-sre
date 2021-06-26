import argparse

parser = argparse.ArgumentParser(
    prog="sre", description="Toolset for service reliability engineering tasks"
)
subparsers = parser.add_subparsers(title="subcommands", description="valid subcommands")

runbook_parser = subparsers.add_parser("runbook")
runbook_parser.add_argument(
    "--name", type=str, required=True, help="runbook(s) to execute"
)

task_parser = subparsers.add_parser("task")
task_parser.add_argument("--name", type=str, required=True, help="task(s) to execute")

output_group = parser.add_mutually_exclusive_group()
output_group.add_argument(
    "--verbose", action="store_true", help="enable verbose output"
)
output_group.add_argument("--silent", action="store_true")

args = parser.parse_args()

print(args)
