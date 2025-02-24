// This component is used to add a new task to the task list
import React, { useState } from "react";
import {
  MDBCard,
  MDBCardBody,
  MDBBtn,
  MDBTooltip,
  MDBIcon
} from "mdb-react-ui-kit";

export default function AddTaskForm({ onCreateTask }) {
  const [taskTitle, setTaskTitle] = useState("");
  const [taskDescription, setTaskDescription] = useState("");
  const [error, setError] = useState("");

  // Create a new task
  const handleCreateTask = () => {
    const titleTrimmed = taskTitle.trim();
    if (!titleTrimmed) {
      setError("Title cannot be empty.");
      // Clear the error message after 3 seconds
      setTimeout(() => {
        setError("");
      }, 3000);
      return;
    }
    setError("");
    onCreateTask(titleTrimmed, taskDescription);
    setTaskTitle("");
    setTaskDescription("");
  };

  return (
    <MDBCard style={{ padding: "1rem" }}>
      <MDBCardBody className="p-2">
        {error && <p className="text-danger small mb-2">{error}</p>}

        <h5 className="mb-2 text-primary">Add Task</h5>
        <div className="d-flex flex-column gap-2">
          <input
            type="text"
            className="form-control form-control-sm"
            placeholder="Title"
            value={taskTitle}
            onChange={(e) => setTaskTitle(e.target.value)}
          />

          <textarea
            className="form-control form-control-sm"
            rows={2}
            placeholder="Description (optional)"
            value={taskDescription}
            onChange={(e) => setTaskDescription(e.target.value)}
          />

          <div className="d-flex align-items-center mt-2">
            <MDBTooltip tag="a" wrapperProps={{ href: "#!" }} title="Set due date">
              <MDBIcon fas icon="calendar-alt" size="lg" className="me-2" />
            </MDBTooltip>
            <MDBBtn size="sm" onClick={handleCreateTask}>
              Add
            </MDBBtn>
          </div>
        </div>
      </MDBCardBody>
    </MDBCard>
  );
}
