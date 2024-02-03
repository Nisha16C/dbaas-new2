<template>
    <div class="card">
      <div class="card-header pb-0 px-3">
        <h6 class="mb-0">Enter the Server Name and Restore Backup.</h6>
      </div>
      <div class="card-body pt-4 p-3">
        <ul class="list-group">
          <li
            class="list-group-item border-0 d-flex p-4 mb-2 bg-gray-100 border-radius-lg"
          >
            <div class="d-flex flex-column">
              <h6 class="mb-3 text-sm">Server and Backup id</h6>
              <form>
                <label class="mb-3 text-sm">Database Name</label>
              <select class="form-select" aria-label="Default select example">
                <option value="15" selected>db-1</option>
                <option value="14">test-23</option>
                <option value="13">postgres</option>
                <option value="12">cluster</option>
              </select>
  
                <div class="form-group mt-3">
                  <label class="text-sm" for=""> Backup id</label>
                  <input
                    type="email"
                    class="form-control"
                    id="Postgres_Username"
                    placeholder="Backup id"
                  />
                </div>
                <div class="form-group mt-3">
                  <label class="text-sm" for=""> Destination Directory</label>
                  <input
                    type="email"
                    class="form-control"
                    id="Postgres_Username"
                    placeholder="Destination directory"
                  />
                </div>
                <div class="form-group mt-3">
                  <label class="text-sm" for=""> Target server Name</label>
                  <input
                    type="email"
                    class="form-control"
                    id="Postgres_Username"
                    placeholder="Target Server"
                  />
                </div>
  
            
              </form>
              </div>
  
          </li>
        </ul>
        <div class="px-2">
        <argon-button color="success" size="md" variant="gradient">
          Restore Backup
        </argon-button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import ArgonButton from "@/components/ArgonButton.vue";
  
  export default {
    name: "billing-card",
    components: {
      ArgonButton,
    },
  };
  </script>
  