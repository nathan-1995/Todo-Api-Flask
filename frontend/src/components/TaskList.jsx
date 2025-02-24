// This component displays a list of tasks. Includes buttons to mark tasks as done.
import React from "react";
import {
  MDBCard,
  MDBCardBody,
  MDBBtn
} from "mdb-react-ui-kit";

// Returns a list of tasks created by the user
export default function TaskList({ tasks, onMarkDone }) {
  return (
    <>
      {tasks.map((task) => (
        <MDBCard
          key={task.id}
          className="mb-2"
          style={{ backgroundColor: "#eeeeee", borderRadius: "8px" }}
        >
          <MDBCardBody className="d-flex justify-content-between align-items-center">
            <div>
              <h5 className="mb-1">{task.title}</h5>
              <p className="mb-0 text-muted">{task.description}</p>
            </div>
            <MDBBtn  color="primary" onClick={() => onMarkDone(task.id)}>

              Done
            </MDBBtn>
          </MDBCardBody>
        </MDBCard>
      ))}
    </>
  );
}
