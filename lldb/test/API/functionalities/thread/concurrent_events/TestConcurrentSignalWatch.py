
import unittest2

from lldbsuite.test.decorators import *
from lldbsuite.test.concurrent_base import ConcurrentEventsBase
from lldbsuite.test.lldbtest import TestBase


@skipIfWindows
class ConcurrentSignalWatch(ConcurrentEventsBase):

    # Atomic sequences are not supported yet for MIPS in LLDB.
    @skipIf(triple='^mips')
    @skipIf(
        oslist=["ios", "watchos", "tvos", "bridgeos", "macosx"],
        archs=['arm64', 'arm64e', 'arm64_32', 'arm'],
        bugnumber="rdar://81811539")
    @add_test_categories(["watchpoint"])
    def test(self):
        """Test a watchpoint and a signal in multiple threads."""
        self.build(dictionary=self.getBuildFlags())
        self.do_thread_actions(num_signal_threads=1, num_watchpoint_threads=1)
