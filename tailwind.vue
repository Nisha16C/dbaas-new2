<!DOCTYPE html>
<html>

<head>
    <title>Select Tools</title>
    <!-- Include Vue.js -->
    <script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.js"></script>
</head>

<body>
    <div id="app">
        <h1>DURGA (Defense Utility for Risk Governance and Awareness)</h1>
        <a class="logout" href="{% url "account_logout" %}"> Logout</a>

        <div class="container">
            <div class="left-panel">
                <div class="op">Select Options</div>

                <!-- Use Vue.js for rendering tool links -->
                <div class="tool-link" v-for="(tool, index) in tools" :key="index" @click="selectTool(tool)">
                    Log
                </div>

                <div class="install-button-container">
                    <input type="submit" id="submit-button" name="submit" value="Install" :disabled="selectedTools.length === 0" />
                </div>
            </div>

            <div class="center-panel">
                <div>
                    <div class="txt1">Welcome To DURGA Platform</div>
                    <div class="txt2">Guarding with Open Source: Your Digital Safehouse</div>
                </div>

                <!-- Use Vue.js for rendering checkboxes -->
                <div id="checkbox-container">
                    <label v-for="(tool, index) in selectedTools" :key="index">
                        <input type="checkbox" :value="tool.name" v-model="selectedToolNames" />
                        {{ tool.name }}
                    </label>
                </div>
            </div>

            <div class="right-panel" style="display: none;">
                <div class="op">Selected Tools</div>
                <div id="summary-container">
                    <p v-for="(toolName, index) in selectedToolNames" :key="index">{{ toolName }}</p>
                </div>
                <div class="install-button-container">
                    <input type="submit" id="submit-button" name="submit" value="Install" :disabled="selectedToolNames.length === 0" />
                </div>
            </div>
        </div>
    </div>

    <script>
        new Vue({
            el: "#app",
            data: {
                tools: [
                    { name: "Thread Detection And Prevention" },
                    { name: "Log Ingestion" },
                    { name: "Log Analysis" },
                    { name: "Backend Storage" },
                    { name: "Visualization" },
                    { name: "Intelligence Enrichment" },
                    { name: "Case Management" },
                    { name: "Automate" },
                    { name: "Investigation" },
                    { name: "Health Monitoring" }
                ],
                selectedTools: [],
                selectedToolNames: []
            },
            methods: {
                selectTool(tool) {
                    if (this.selectedTools.includes(tool)) {
                        this.selectedTools = this.selectedTools.filter(item => item !== tool);
                    } else {
                        this.selectedTools.push(tool);
                    }
                }
            }
        });
    </script>
</body>

</html>

































<!-- <!DOCTYPE html>
<html>
<head>
    <title>Vue Checkbox Value</title>
    <script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.js"></script>
</head>
<body>
    <div id="app">
        <h1>Vue Checkbox Value:</h1>
        <input type="checkbox" id="checkbox1" value="Option 1" v-model="checkboxes.option1"> Option 1
        <br>
        <input type="checkbox" id="checkbox2" value="Option 2" v-model="checkboxes.option2"> Option 2
        <br>
        <input type="checkbox" id="checkbox3" value="Option 3" v-model="checkboxes.option3"> Option 3
        <br>
        <p>Selected values: {{ selectedValues }}</p>
    </div>

    <script>
        new Vue({
            el: '#app',
            data: {
                checkboxes: {
                    option1: false,
                    option2: false,
                    option3: false
                }
            },
            computed: {
                selectedValues() {
                    const selected = [];
                    for (const key in this.checkboxes) {
                        if (this.checkboxes[key]) {
                            selected.push(key);
                        }
                    }
                    return selected.length > 0 ? selected.join(", ") : 'No checkboxes selected.';
                }
            },
            watch: {
                checkboxes: {
                    deep: true,
                    handler(newVal) {
                        // Update localStorage when checkboxes change
                        for (const key in newVal) {
                            if (newVal.hasOwnProperty(key)) {
                                if (newVal[key]) {
                                    localStorage.setItem(key, 'checked');
                                } else {
                                    localStorage.removeItem(key);
                                }
                            }
                        }
                    }
                }
            },
            mounted() {
                // Load checkbox state from localStorage on component mount
                for (const key in this.checkboxes) {
                    if (localStorage.getItem(key) === 'checked') {
                        this.checkboxes[key] = true;
                    }
                }
            }
        });
    </script>
</body>
</html> -->
