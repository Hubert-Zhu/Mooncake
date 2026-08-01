# Copyright 2024 KVCache.AI
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
import warnings

from mooncake.store import MooncakeDistributedStore


class TestInitAllDeprecation(unittest.TestCase):
    def test_init_all_emits_deprecation_warning(self):
        store = MooncakeDistributedStore()

        with warnings.catch_warnings():
            warnings.simplefilter("error", DeprecationWarning)
            with self.assertRaisesRegex(
                DeprecationWarning,
                r"init_all\(\) is deprecated; use setup\(\) instead",
            ):
                store.init_all("tcp", "", 16 * 1024 * 1024)


if __name__ == "__main__":
    unittest.main()
