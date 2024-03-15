<template>
    <div class="markdown-content">
    <div  id= "htmlContent">
       
        
      <h1><img :src="require('@/Documentation/logo1.png')" class="custom-logo">  Documentation of BitBlast </h1><br>
      
      <p>Let's dive in BitBlast, your comprehensive platform for efficient project management. BitBlast offers a powerful suite of tools, including both the Admin and User Dashboards, designed to streamline collaboration and organization in your projects.</p>
  
      <h4 class="get">Get started today with BitBlast and revolutionize your project management.</h4>
      <p><a href=" " class="link">BitBlast url</a></p>
       <div>
        <button @click="downloadPDF" class="pdf-download-button">Download PDF</button>
        </div>
      <hr>
 
      <h2>Feature of Application</h2>
      <ol>
          <li>   <p><b>User Authentication:</b> User Authentication is a fundamental aspect of BitBlast that ensures secure and personalized access to the platform. It involves the verification of user credentials to guarantee that only authorized individuals can log in and interact with the system.</p>
          </li>
          <li>    
              <p><b>User-Friendly Interface:</b> BitBlast prides itself on providing a User-Friendly Interface, making the platform accessible and intuitive for users of all levels of expertise. The interface is designed with the user's convenience in mind, promoting ease of navigation and interaction.</p>
          </li>
          <li> 
              <p><b>Project and Cluster Creation:</b> BitBlast simplifies Project and Cluster Creation, allowing users to set up and manage their workspaces efficiently. This involves initiating new projects and creating clusters (databases) to organize and store project-related data.</p>
          </li>
          <li> <p><b>Multi-Cluster Creation:</b> Multi-Cluster Creation is a feature that extends the capabilities of BitBlast, allowing users to create and manage multiple clusters simultaneously. This is particularly useful for users engaged in complex projects that require diverse sets of data organization.</p>
          </li>
          <li>  
              <p><b>Multi-Cloud Support:</b> BitBlast boasts Multi-Cloud Support, enabling users to integrate and work seamlessly across different cloud providers. This feature provides flexibility in choosing the cloud environment that best suits the project's needs.</p>
          </li> 
      </ol>
 
      <h2>Characteristics of Application</h2>
  
      <ol>
          <li>Centralized control, Deletion, and monitoring of clusters.</li>
          <li>Streamlined organization and tracking of projects within clusters and User-friendly project editing functionality.</li>
          <li>Convenient user administration with the ability to create new users.</li>
          <li>Comprehensive audit trail for security, accountability, detailed tracking, and filtering of user activities.</li>
          <li>Secure login mechanisms for user authentication.</li>
          <li>Facilitates the creation of new projects.</li>
          <li>Supports the creation of multiple clusters for effective organization.</li>
          <li>Assignment of projects to specific clusters during creation.</li>
          <li>Compatibility with various cloud service providers.</li>
          <li>User choice of preferred cloud provider during cluster creation.</li>
          <li>Cloud-agnostic features for seamless deployment across different cloud environments.</li>
      </ol>

      <h2>Benefits of Application</h2>
        <ol>
            <li><b>Scalability:</b> BitBlast offers seamless scalability, allowing you to handle fluctuations in data volume without any hassle.</li>
            <li><b>High Availability:</b> With built-in redundancy and failover mechanisms, BitBlast ensures high availability for your critical data.</li>
            <li><b>Security:</b> Utilizing advanced encryption techniques and strict access controls, BitBlast keeps your data safe and compliant.</li>
            <li><b>Automated Backups:</b> BitBlast automates the backup process, providing peace of mind against data loss.</li>
            <li><b>Multi-Cloud Support:</b> BitBlast supports multiple cloud providers, offering flexibility and vendor lock-in avoidance.</li>
            <li><b>Performance Optimization:</b> BitBlast optimizes database performance through intelligent caching and indexing strategies.</li>
            <li><b>Real-time Monitoring:</b> Keep track of your database performance and health in real-time with BitBlast's monitoring dashboard.</li>
        </ol>

      <h2>How to get started with BitBlast</h2>
      <p>The login functionality of BitBlast is a pivotal aspect of the platform's user authentication process, ensuring a secure and personalized
         experience for each user. To access BitBlast, users are required to input their unique and authorized credentials, including a secure username 
         and password. The login functionality is designed with an emphasis on user privacy and data protection, employing encryption protocols to 
         secure the transmission of login information. Once authenticated, users gain access to their personalized dashboards, 
         whether it be the Admin Dashboard or User Dashboard, depending on their role. This approach ensures that only authorized personnel can access
          and navigate the powerful features and tools within BitBlast. Overall, the login functionality not only establishes a secure 
          gateway to the platform but also plays a crucial role in tailoring the BitBlast experience to the specific needs of each user.</p>
           <p>We have two Dashboards - 1) User Dashboard 2) Admin Dashboard</p>

        <h2>User Dashboard</h2>
        <p>The User Dashboard is your personalized space for seamless project engagement and collaboration. 
            The User Dashboard empowers you to contribute actively to project management, 
            enabling the creation and management of clusters and the initiation of new projects.</p>
        <h4>1. Login to Account -</h4>
        <p>As a user, accessing your dashboard is straightforward. Simply log in with your authorized credentials,
                including your secure username, password and click 'sign in'.
                This ensures a secure entry, protecting your project-related information within the BitBlast platform.</p><br>
                <img :src="require('@/Documentation/img1.png')" class="custom-image"><br><br><hr>
       
        <h4>2. Select Project</h4>
        <p>By default, a project is automatically assigned to you by admin, making it convenient
             to start working right away. However, if you prefer to create your 
             own project or switch to another one, BitBlast offers flexibility.</p>
        <p>As a new user, BitBlast automatically assigns a default project to streamline 
            your onboarding experience. This allows you to dive into your work immediately without the need for
             manual project selection.</p>
        <p>"Additionally, at any point, you can visit the 'Project-Select Page' to view t all available projects. Here, you have the 
            freedom to select a different project based on your preferences or work requirements."</p>
            <img :src="require('@/Documentation/img2.png')" class="custom-image" ><br><br><hr>


        <h4>3. Overview </h4>
        <p>The Overview page in BitBlast provides a consolidated snapshot of your project landscape. Here, you can effortlessly view the total number of clusters and projects at a glance. It serves as a central hub, offering a quick and comprehensive overview of your project ecosystem, allowing you to gauge the scale and scope of your current endeavors. This streamlined presentation on the Overview page ensures that crucial information about the number of clusters and 
            projects is readily available for efficient decision-making and project management.</p>
            <img :src="require('@/Documentation/img21.png')" class="custom-image" ><br><br><hr>
        
        <h4>4. Project </h4>
        <p>The Project Page in BitBlast is your dedicated space for project management. Here, you have a comprehensive overview of your projects, the ability to create new projects seamlessly,
             and access to essential details about each project.</p>
        <p>"At the top of the Project Page, you'll find a clear count of the total number of projects currently active in BitBlast. This gives 
                you an instant understanding of the scope and scale of your ongoing projects."</p>
        <p>"Empowering you to initiate new projects is the 'Create Project' feature.
             Simply type the desired name into the input field and, with a click on the 'Create Project' button, 
            you can seamlessly add a new project to your BitBlast environment."</p>
        <p>"As you scroll down, you'll encounter a comprehensive list of all projects within BitBlast. Each project 
            entry includes its unique ID, project name, created date, and last updated date,"</p>
        <p>"The Project Page allowing you to monitor existing projects, create new ones effortlessly, 
            and access critical details about each project for efficient project management."</p>
            <img :src="require('@/Documentation/img16.png')" class="custom-image" ><br><br><hr>
        
        <h4>5. Providers </h4>
        <p>BitBlast simplifies the process of creating databases or clusters by requiring users to first add providers. Providers play a crucial role in defining the infrastructure for these clusters. By adding providers, users can establish the foundation for their databases, ensuring compatibility and optimization. This initial step streamlines the subsequent creation process, allowing users to seamlessly configure and customize their clusters. BitBlast's approach ensures that the addition of providers is the first step in creating robust
             and tailored database clusters, providing a user-friendly and efficient experience.</p>
             <img :src="require('@/Documentation/img13.png')" class="custom-image" ><br><br>
        <p>BitBlast offers a straightforward approach to adding providers and creating clusters. Users can select the desired provider and fill in its specific fields, including API Name, API Endpoint, Access Key, and Secret Key. Once these details are entered, clicking the "Add Provider" button seamlessly incorporates the chosen provider into BitBlast's system. This user-friendly process ensures that users can efficiently add providers, providing the necessary infrastructure for creating clusters. The intuitive design of BitBlast empowers users to effortlessly configure providers and proceed
             with the creation of customized and optimized clusters within their projects.</p>
             <img :src="require('@/Documentation/img14.png')" class="custom-image" ><br><br><hr>

        <h4>6. Cluster </h4>
        <p>BitBlast's Cluster page is designed to provide a comprehensive view of your project's clusters and databases. On this page, you can easily access the total number of clusters,
             giving you an immediate understanding of your project's infrastructure scale apart is its "All Project" dropdown feature, enabling users to filter databases by project. This functionality allows users to focus on specific projects and view their associated databases.</p>
        <p>Additionally, the Cluster page displays a detailed list of all databases associated with each cluster. This list includes essential information such as the name and ID of each database, along with their respective creation and update dates. This organized presentation ensures that you have a clear and up-to-date overview of your database assets, 
            facilitating efficient management and decision-making within your project.</p> 
            <img :src="require('@/Documentation/img10.png')" class="custom-image" ><br><br>
        <h6 class="data">Create CloudStack Clusters</h6>
        <p><b>Create Database/Cluster : </b>BitBlast simplifies the process of creating a new database or cluster with the convenience of the "Create New Cluster" button.
             By clicking this button, users can initiate the setup for a fresh database cluster seamlessly. 
             This feature streamlines the creation process, guiding users through the necessary steps to establish a new cluster within their project.
              Whether it's for expanding projects, accommodating additional data, or organizing information more efficiently, the "Create New Cluster" button is your gateway
             to a straightforward and user-friendly database creation experience in BitBlast.</p>
             <img :src="require('@/Documentation/img10.png')" class="custom-image" ><br><br>
        
        <p>BitBlast ensures a smooth transition from clicking the "Create New Cluster" button to the "Cluster Info" page. On this page, users can seamlessly proceed by selecting the Cluster Type and Providers, offering a range of options including CloudStack, Harvester, OpenStack, VMware, Nutanix, and Kubernetes. Once the desired configurations are chosen, clicking the "Next" button initiates the process, guiding users through the subsequent steps for creating a new cluster. This user-friendly interface and step-by-step approach empower users to customize their clusters according to specific needs,
             ensuring a tailored and efficient database creation experience in BitBlast.</p>
             <img :src="require('@/Documentation/MicrosoftTeams-image (16).png')" class="custom-image" ><br><br>
        <p>After clicking the "Next" button, users are directed to the DB Configuration page in BitBlast. Here, they encounter the option to choose a "compute resource," such as a small or medium instance. Following this selection, users proceed to define volume properties in the "Custom Storage" section, specifying the desired storage capacity. Once these steps are completed, users can click the "Next" button to proceed to the Cluster Setting page, advancing further in the process of creating their cluster.
             This streamlined process ensures that users can configure their cluster resources efficiently and tailor them to their project requirements within BitBlast.</p>
             <img :src="require('@/Documentation/MicrosoftTeams-image (15).png')" class="custom-image" ><br><br>

        <p>Upon clicking the "Next" button on the "DB Configuration" page, BitBlast seamlessly directs users to the "Cluster Setting" page. Here, users can input essential details such as the Cluster Name, Postgres username, Password, Database version, and Backup Method. The intuitive design allows users to customize these settings according to their project requirements. After filling in the necessary information, users can view all cluster details in the Cluster Summary section, including cluster type, cluster nodes, providers, Postgres type, instance type, volume type, volume properties, and networking.
             Clicking the "Create Cluster" button.</p>  
            <img :src="require('@/Documentation/MicrosoftTeams-image (13).png')" class="custom-image" ><br><br>
        <p>After clicking the "Create Cluster" button,BitBlast displays the progress status of the database creation process. 
            Users can track the progress as the system sets up the database infrastructure.Here, users may need to wait for the progress to complete, which typically takes 2-3 minutes. During this time, the system is actively processing the requested operation,  </p>
            <img :src="require('@/Documentation/MicrosoftTeams-image (14).png')" class="custom-image" ><br><br>
        <p>Once the progress is complete and the database is successfully created, 
            BitBlast promptly presents users with the credentials required to access the newly created database. This includes essential information such as the Database Name , Database User, password, and any other relevant details needed for database access.
             With this streamlined process, BitBlast ensures users are promptly equipped with the necessary credentials to begin utilizing their newly created database.</p>
            <img :src="require('@/Documentation/MicrosoftTeams-image (10).png')" class="custom-image" ><br><br>



        <p><b>view Database Information : </b>By clicking the "View" button on BitBlast's Cluster page, you gain access to a wealth of information related to the selected database. This includes detailed insights into artifacts and dynamic data associated with that specific database. Whether it's examining specific artifacts or exploring dynamic data points, the "View" feature empowers you to delve into the intricacies of the database, providing a comprehensive understanding of its contents. This functionality enhances your ability to analyze and manage the database effectively, ensuring that 
            you have the necessary insights to make informed decisions within your project.</p>
            <img :src="require('@/Documentation/img23.png')" class="custom-image" ><br><br>

        <p><b>Delete Database : </b>Upon clicking the "Delete" button on BitBlast's Cluster page, users initiate the deletion process for the selected database. BitBlast then displays the progress of the deletion, allowing users to track its completion. Once the progress bar reaches completion, indicating that the deletion process is finished, the selected database is permanently removed from the project's database infrastructure. It's
             important to exercise caution when utilizing this feature, as it results in the irreversible removal of the database and its associated data from the project.</p>
            <img :src="require('@/Documentation/MicrosoftTeams-image (9).png')" class="custom-image" ><br><br>
            <img :src="require('@/Documentation/MicrosoftTeams-image (2).png')" class="custom-image"><br><br>

        <h6 class="data">Create Kubernetes Clusters</h6>
        <p><b>Create Database/Cluster : </b> BitBlast simplifies the process of creating kubernetes new database or cluster with the convenience of the "Create Cluster" button. By clicking this button, users can initiate the setup for a fresh database cluster seamlessly. This feature streamlines the creation process, guiding users through the necessary steps to establish a new cluster within their project. Whether it's for expanding projects, accommodating additional data, or organizing information more efficiently, the "Create Cluster" button is your gateway
             to a straightforward and user-friendly database creation experience in BitBlast.</p>
             <img :src="require('@/Documentation/img10.png')" class="custom-image" ><br><br>
       
        <p>BitBlast ensures a smooth transition from clicking the "Create Cluster" button to the "Cluster Info" page. On this page, users can seamlessly proceed by selecting the Cluster Type and Providers, offering a range of options including CloudStack, Harvester, OpenStack, VMware, Nutanix, and Kubernetes. Once the desired configurations are chosen, clicking the "Next" button initiates the process, guiding users through the subsequent steps for creating a new cluster. This user-friendly interface and step-by-step approach empower users to customize their clusters according to specific needs,
             ensuring a tailored and efficient database creation experience in BitBlast.</p>
             <img :src="require('@/Documentation/MicrosoftTeams-image (7).png')" class="custom-image"><br><br>
        
        <p>Upon clicking the "Next" button on the "Cluster info" page, BitBlast seamlessly directs users to the "Cluster Setting" page. Here, users can input essential details such as the Cluster Name, Postgres username, Password, Database version, and Backup Method. The intuitive design allows users to customize these settings according to their project requirements. After filling in the necessary information, users can view all cluster details in the Cluster Summary section, including cluster type, cluster nodes, providers, Postgres type, instance type, volume type, volume properties, and networking.
             Clicking the "Next" button progresses users to the subsequent steps, facilitating a smooth and guided process for configuring cluster settings in BitBlast.</p>  
             <img :src="require('@/Documentation/img24.png')" class="custom-image"><br><br> 
       
        <p>After clicking the "Create Cluster" button,BitBlast displays the progress status of the database creation process. 
            Users can track the progress as the system sets up the database infrastructure. </p>
            <img :src="require('@/Documentation/MicrosoftTeams-image (12).png')" class="custom-image"><br><br>
        
        <p>Once the progress is complete and the database is successfully created, 
            BitBlast promptly presents users with the credentials required to access the newly created database. This includes essential information such as the Database Name , Database User, password, and any other relevant details needed for database access.
             With this streamlined process, BitBlast ensures users are promptly equipped with the necessary credentials to begin utilizing their newly created database.</p>
             <img :src="require('@/Documentation/MicrosoftTeams-image (1).png')" class="custom-image"><br><br> 
             
             <p><b>view Database Information : </b>By clicking the "View" button on BitBlast's Cluster page, you gain access to a wealth of information related to the selected database. This includes detailed insights into artifacts and dynamic data associated with that specific database. Whether it's examining specific artifacts or exploring dynamic data points, the "View" feature empowers you to delve into the intricacies of the database, providing a comprehensive understanding of its contents. This functionality enhances your ability to analyze and manage the database effectively, ensuring that 
            you have the necessary insights to make informed decisions within your project.</p> 
        <img :src="require('@/Documentation/MicrosoftTeams-image (4).png')" class="custom-image"><br><br>

        <p><b>Delete Database : </b>Upon clicking the "Delete" button on BitBlast's Cluster page, users initiate the deletion process for the selected database. BitBlast then displays the progress of the deletion, allowing users to track its completion. Once the progress bar reaches completion, indicating that the deletion process is finished, the selected database is permanently removed from the project's database infrastructure. It's
             important to exercise caution when utilizing this feature, as it results in the irreversible removal of the database and its associated data from the project.</p>
          
        <img :src="require('@/Documentation/MicrosoftTeams-image (3).png')" class="custom-image"><br><br>
        <img :src="require('@/Documentation/MicrosoftTeams-image (2).png')" class="custom-image"><br><br><hr>
        




        <h2>Admin Dashboard</h2>
        <p>Before we dive into the login process, let's understand the Admin Dashboard. 
            This dashboard serves as the control center, allowing administrators to oversee and 
            manage crucial components such as clusters, projects, and users. Now, let's explore 
            how administrators can log in and unleash the full potential of the Admin Dashboard.</p>

        <h4>1. Login to Admin Account  </h4>
        <p>To log in to the Admin Dashboard, administrators need to visit the BitBlast login page. Here, they'll input their authorized credentials - a secure username and password. This ensures that only
             authorized personnel gain access to the powerful administrative features of BitBlast.</p>
             <img :src="require('@/Documentation/img17.png')" class="custom-image" ><br><br><hr>

        <h4>2. Admin Dashboard </h4>
        <p>Welcome to the Admin Dashboard of BitBlast, your central command center for seamless project management. Here, you have a comprehensive overview of essential elements - 
            the total number of clusters, projects, and users, all in one place.</p>
            <img :src="require('@/Documentation/img18.png')" class="custom-image" ><br><br><hr>
        
        <h4>3. Clusters Management </h4>
        <p>"Let's dive into Cluster Management, your control center for overseeing and organizing clusters in BitBlast.
             Here, you get a quick overview of the total number of clusters available."</p>
        <p>"In the Cluster Management page, you have access to detailed information about
            each database. This includes the Database Name and ID, Database Type and Version, 
            Provider Name, Created Date, and Updated Date."</p>
            <img :src="require('@/Documentation/img19.png')" class="custom-image" ><br><br>
        
        <p><b>View Database Information : </b>With the 'View' button, you can drill down
             into specific database details. Clicking on 'View' allows you to access comprehensive information related to any particular
             database, including its artifacts and dynamic data.</p>
             <img :src="require('@/Documentation/img25.png')" class="custom-image" ><br><br>

        <p><b>Delete Database : </b>"Need to tidy up your database landscape? The 'Delete' button empowers you to I remove any unwanted databases efficiently. A simple click on 'Delete,' and
             you can seamlessly eliminate a database from the system."</p>
             <img :src="require('@/Documentation/img4.png')" class="custom-image" ><br><br>
        
             <p> Cluster Management in BitBlast provides a centralized space for not only viewing the total number of clusters but also detailed insights into each database. With the ability to view and delete databases,
                 you have the b control to streamline and manage your database environment effectively.</p><br><br><hr>

        <h4>4. Project Management </h4>
        <p>Project Management is the space where you have complete control over your projects in BitBlast.
             Let's start by getting an overview of the total number of projects available.</p>

        <p>"In the Project Management page, you can access detailed information about each project, including the Project Name and ID, Created Date, and Updated Date."</p>
        <img :src="require('@/Documentation/img5.png')" class="custom-image" ><br><br>

        <p><b>Rename Project : </b>Need to refine a project's identity? The 'Edit' button allows you to rename In any project seamlessly. A quick click on 'Edit',
             and you can update the name of your project for better clarity.</p>
             <img :src="require('@/Documentation/img6.png')" class="custom-image" ><br><br>

        <p>Project Management in BitBlast provides not only a quick glance at the total number of projects but also offers detailed insights into each project. With the ability to edit and rename projects,
             you have the flexibility to keep your project organization precise and up-to-date.</p><hr>

        <h4>5. User  Management </h4>
        <p>Let's explore User Management, the central hub for overseeing and organizing users in BitBlast.
             Begin by getting an overview of the total number of users available.</p>

        <p>"In the User Management page, detailed information about each user is at your fingertips. This includes the User Name and ID,
             Status (active or inactive), Created Date, Last Login, and Email Address."</p>
             <img :src="require('@/Documentation/img7.png')" class="custom-image" ><br><br>

        <p><b>New User Creation : </b>"Want to add a new member to your team? The 'Create New User' button allows you to seamlessly add a new user. Clicking on it opens a form where you can input information such as First Name, Last Name, Username, 
            Phone Number, Emails Address, Password, and agree to the terms & conditions."</p>
            <img :src="require('@/Documentation/img8.png')" class="custom-image" ><br><br>
        
        <p>"Ater successfully creating a new user, you'll receive a confirmation message. This message indicates 
            that the new user has been added successfully and is now visible in the user table."</p>
        
        <p>User Management in BitBlast not only provides an overview of the total number of users but also offers detailed insights into each user. With the ability to create new users, you have
             the flexibility to manage your team efficiently and keep user information up-to-date."</p>
            <hr>

        <h4>6. Monitoring </h4>
        <p>The monitoring dashboard in BitBlast provides users with detailed insights into their clusters and databases, allowing for efficient management and optimization. Users can access a wide range of information related to specific users' databases, including cluster type, database version, start time, and various performance metrics such as average CPU and memory usage. Additionally, users can monitor important metrics like open file descriptors, shared buffers, and active sessions in real-time, enabling proactive decision-making and troubleshooting. With comprehensive data on transactions, update data, fetch data, 
            insert data, and lock tables, the monitoring dashboard empowers users to maintain optimal performance and reliability across their database. </p>
        <img :src="require('@/Documentation/img20.png')" class="custom-image" ><hr>

        <h4>7. Backup </h4><hr>

        <h4>8. Activity Logs </h4>
        <p>Activity Logs in BitBlast serve as a comprehensive record of all actions and events within the platform, offering transparency and accountability. This log captures every significant activity, allowing users, especially administrators, to monitor and audit changes effectively. The Activity Logs encompass a variety of events, including user logins, 
            new user creations, project and cluster modifications, and database deletions.</p>

        <p>For instance, when a user logs in, BitBlast records this event in the Activity Logs, providing information about who accessed the platform and when. Similarly, if a new user is created, the log details the user's information and the timestamp of the creation. Project and cluster modifications, such as renaming projects or creating new clusters, 
            are also documented, offering a comprehensive history of changes.</p>

        <p>The deletion of a database or cluster is another event captured in the Activity Logs. This feature ensures that administrators can trace and understand every action, fostering a secure and accountable environment. The Activity Logs in BitBlast thus play a pivotal role in enhancing governance, 
            security, and monitoring capabilities within the platform.</p>
            <img :src="require('@/Documentation/img9.png')" class="custom-image" ><br><br>
        
        <p>BitBlast's Activity Logs provide a concise and detailed summary of all platform activities, offering administrators a transparent view of user actions. From user logins to project and cluster modifications, every event is meticulously recorded, ensuring accountability. The logs serve as a valuable tool for monitoring user activity, tracking changes, and maintaining a secure and auditable project environment. With a focus on transparency,
                 BitBlast's Activity Logs enhance governance and security within the platform.</p><hr>

    </div>
</div>
  </template>
<script>

import html2pdf from 'html2pdf.js';

export default {
  methods: {

    downloadPDF() {
        // window.print()
      html2pdf(document.getElementById('htmlContent'), {
        margin:       1,
        filename:     'BitBlast-Document.pdf',
        // image:        { type: 'png', quality: 0.98 },
        // html2canvas:  { scale: 2 },
        // jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
      });
      
    }
  }
}
</script>
  
  <style scoped>
  /* Update styles for the markdown content */
  .markdown-content {
    margin: 70px;
    padding: 50px;
    border: 1px solid white;
    background-color:white;
    color: black;
    border-radius: 20px;
  }
  .custom-image {
  width: 1000px;
  height: 500px;
  border: 1px solid #ccc;
  border-radius: 1px;
  /* display: block;
  margin-left: auto; 
  margin-right: auto;  */
}
.custom-logo {
  width: 150;
  height: 75px;
  /* border: 1px solid #ccc; */
  /* border-radius: 1px; */
  /* display: block;
  margin-left: auto; 
  margin-right: auto;  */
}
/* .pdf-download-container {
  position: fixed;
  top: 20px; 
  right: 20px;
} */

.pdf-download-button {
  background-color: #20c997;
  color: white;
  border: none;
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
}
.link {
    color : blue;
}
.get {
    color: rgb(93, 56, 128);
}
.data {
    color: rgb(97, 3, 185);
    text-decoration: underline;
}
  </style>