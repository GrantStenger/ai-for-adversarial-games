export default function checkWin(gameState) {
  var player1PromotedPieces = 0;
  for (let row = 0; row < 5; row++) {
    for (let column = 5 + row; column < 9; column++) {
      if (gameState[row][column] === 1) {
        player1PromotedPieces++;
      }
    }
  }
  if (player1PromotedPieces === 10) {
    return 1;
  }

  var player2PromotedPieces = 0;
  for (let row = 4; row < 9; row++) {
    for (let column = 0; column < row - 4; column++) {
      if (gameState[row][column] === 2) {
        player2PromotedPieces++;
      }
    }
  }
  if (player2PromotedPieces === 10) {
    return 2;
  }

  return 0;
}
