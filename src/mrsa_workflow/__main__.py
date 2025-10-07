# SPDX-FileCopyrightText: 2025-present John Sundh <john.sundh@scilifelab.se>
#
# SPDX-License-Identifier: MIT
import sys

if __name__ == "__main__":
    from mrsa_workflow.cli import mrsa_workflow

    sys.exit(mrsa_workflow())
