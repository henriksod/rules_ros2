# Copyright 2023 Milan Vukov
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest

import launch.actions
import launch_ros.actions
import launch_testing.actions
import launch_testing.asserts


def generate_test_description():
    test_node = launch_ros.actions.Node(
        executable='third_party/foxglove_bridge/foxglove_bridge_tests',
        output='screen',
    )

    return (
        launch.LaunchDescription([
            # ROS_DISTRO is necessary for correct operation of the Foxglove
            # Studio.
            launch.actions.SetEnvironmentVariable(name='ROS_DISTRO',
                                                  value='humble'),
            test_node,
            launch_testing.actions.ReadyToTest(),
        ]),
        {
            'test_node': test_node,
        })


class TestFoxgloveBridge(unittest.TestCase):

    def test_talker_tests(self, proc_info, test_node):
        proc_info.assertWaitForShutdown(process=test_node, timeout=5)
        launch_testing.asserts.assertExitCodes(
            proc_info,
            allowable_exit_codes=[launch_testing.asserts.EXIT_OK],
            process=test_node)
