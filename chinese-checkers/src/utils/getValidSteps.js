import isValidStep from "./isValidStep";

export default function getValidSteps(gameState, playerID) {
  let validSteps = [];
  for (let startRow = 0; startRow < 9; startRow++) {
    for (let startColumn = 0; startColumn < 9; startColumn++) {
      for (let endRow = 0; endRow < 9; endRow++) {
        for (let endColumn = 0; endColumn < 9; endColumn++) {
          if (
            isValidStep(
              gameState,
              playerID,
              startRow,
              startColumn,
              endRow,
              endColumn
            )
          ) {
            validSteps = [
              ...validSteps,
              [startRow, startColumn, endRow, endColumn],
            ];
          }
        }
      }
    }
  }
  return validSteps;
}
