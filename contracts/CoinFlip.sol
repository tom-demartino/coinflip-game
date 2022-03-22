// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0;

contract CoinFlip {
   // return
   //    0 = heads, 1 = tails
   function _flip() private view returns (bool) {
      return uint(keccak256(abi.encodePacked(block.timestamp))) % 2 == 1;
   }

   // arguments
   //    guess: 0 = head, 1 = tails
   // return
   //    win: 0 = lose, 1 = win
   function flip(bool guess) public view returns (bool) {
      return guess == _flip();
   }
}