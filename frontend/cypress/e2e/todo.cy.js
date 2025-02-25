describe('Front End Task Test', () => {
  it('allow a user to add a task and return task in list', () => {
    // Listen for GET requests to the /tasks endpoint
    cy.intercept('GET', '**/tasks').as('getTasks');

    // Go to frontend
    cy.visit('http://localhost:5173');

    // Fill out the add task form
    cy.get('input[placeholder="Title"]').type('Cypress Test Task');
    cy.get('textarea[placeholder="Description (optional)"]').type('Cypress Test Task Description');

    // Click the Add button
    cy.contains('button', 'Add').click();

    // Wait for the GET request to complete which should update the task list
    cy.wait('@getTasks');

    // Verify the new task is visible in the list
    cy.contains('Cypress Test Task').should('be.visible');
    cy.contains('Cypress Test Task Description').should('be.visible');
  });
});
