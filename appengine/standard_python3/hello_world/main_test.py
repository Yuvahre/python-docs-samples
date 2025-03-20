# Copyright 2018 Google Inc.
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
import main

def test_convert():
    main.app.testing = True
    client = main.app.test_client()
    
    # Test Celsius to Fahrenheit conversion
    response = client.post("/", data={"temperature": "100", "unit": "C"})
    assert response.status_code == 200
    assert "212.00 °F" in response.data.decode("utf-8")
    
    # Test Fahrenheit to Celsius conversion
    response = client.post("/", data={"temperature": "32", "unit": "F"})
    assert response.status_code == 200
    assert "0.00 °C" in response.data.decode("utf-8")
    
    # Test invalid input
    response = client.post("/", data={"temperature": "abc", "unit": "C"})
    assert response.status_code == 200
    assert "Invalid Input" in response.data.decode("utf-8")
    assert "Hello World" in r.data.decode("utf-8")
