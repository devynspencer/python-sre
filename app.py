import argparse

parser = argparse.ArgumentParser(
    prog="sre", description="Toolset for service reliability engineering tasks"
)
parser.add_argument("--runbook", type=str, help="runbook(s) to execute")
parser.add_argument("--task", type=str, help="task(s) to execute")
parser.add_argument("--verbose", action="store_true", help="enable verbose output")
parser.add_argument("--silent", action="store_true")

args = parser.parse_args()

if args.runbook is not None:
    print(args.runbook)

if args.task is not None:
    print(args.task)
