# Copyright (c) 2016 Dataman Cloud
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


class AuthMixin(object):
    """Auth associated apis"""

    def get_token(self, name, passwd):
        """List user info from token"""

        data = {
            "name": name,
            "password": passwd
        }

        resp = self.http.post("/auth", data=data)

        return self.process_data(resp)

    def delete_token(self):
        resp = self.http.delete("/auth")
        return self.process_data(resp)
