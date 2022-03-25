// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0;

contract CoinFlip {
   // Event posted to chain that details result of coinflip
   event Result(address indexed _from, bool _guess, bool _win);

   // return
   //    0 = heads, 1 = tails
   function _flip() private view returns (bool) {
      return uint(keccak256(abi.encodePacked(block.timestamp))) % 2 == 1;
   }

   // arguments
   //    guess: 0 = head, 1 = tails
   // return
   //    win: 0 = lose, 1 = win
   function flip(bool _guess) public returns (bool) {
      bool win = _guess == _flip();
      emit Result(msg.sender, _guess, win);
      return win;
   }
}