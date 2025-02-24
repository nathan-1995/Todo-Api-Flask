// App.jsx

import React, { useState, useEffect } from "react";
import {
  MDBContainer,
  MDBRow,
  MDBCol,
  MDBCard,
  MDBCardBody,
  MDBIcon,
} from "mdb-react-ui-kit";

// Services and Components
import { getTasks, createTask, markTaskDone } from "./services/taskService";
import AddTaskForm from "./components/AddTaskForm";
import TaskList from "./components/TaskList";

export default function App() {
  const backendUrl = import.meta.env.VITE_BACKEND_URL; // Backend URL from environment variables
  const [tasks, setTasks] = useState([]); // State to hold the list of tasks

  // Fetch tasks when the component loads
  useEffect(() => {
    loadTasks();
  }, []);

  // Load tasks from the server 
  const loadTasks = async () => {
    try {
      const data = await getTasks(backendUrl);
      setTasks(data);
    } catch (err) {
      console.error("Error fetching tasks:", err);
    }
  };

  // Create a new task and reload the task list
  const handleCreateTask = async (title, description) => {
    try {
      await createTask(backendUrl, title, description);
      await loadTasks();
    } catch (err) {
      console.error("Error creating task:", err);
    }
  };

  // Mark a task as completed and reload the task list
  const handleMarkDone = async (taskId) => {
    try {
      await markTaskDone(backendUrl, taskId);
      await loadTasks();
    } catch (err) {
      console.error("Error updating task:", err);
    }
  };

  return (
    // Main element
    <MDBContainer className="py-3">
      <MDBRow className="d-flex justify-content-center align-items-center h-100">
        <MDBCol>
          <MDBCard
            id="list1"
            style={{ borderRadius: ".75rem", backgroundColor: "#eff1f2" }}
          >
            <MDBCardBody className="py-4 px-4 px-md-5">
              {/* Form to add tasks */}
              <div className="pb-2">
                <AddTaskForm onCreateTask={handleCreateTask} />
              </div>

              <hr className="my-4" />

              {/* List of tasks */}
              <TaskList tasks={tasks} onMarkDone={handleMarkDone} />
            </MDBCardBody>
          </MDBCard>
        </MDBCol>
      </MDBRow>
    </MDBContainer>
  );
}
