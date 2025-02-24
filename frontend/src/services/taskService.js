// This file contains functions that interact with the backend to fetch and create tasks
export async function getTasks(backendUrl) {
    const res = await fetch(`${backendUrl}/tasks`);
    return res.json();
  }
  
  // Creates a new task with a given title and description
  export async function createTask(backendUrl, title, description = "") {
    const body = { title, description };
    const res = await fetch(`${backendUrl}/tasks`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });
    return res.json();
  }
  
  /**
   * Marks a specific task as completed.
   */
  export async function markTaskDone(backendUrl, taskId) {
    const res = await fetch(`${backendUrl}/tasks/${taskId}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ completed: true }),
    });
    return res.json();
  }
  