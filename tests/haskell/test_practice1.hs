-- Tests for solutions/haskell/practice1.hs (Calculate Digit Sum of a String)
-- Load in GHCi: :load solutions/haskell/practice1.hs tests/haskell/test_practice1.hs
module Main where

import Control.Monad (unless)
import System.Exit (exitFailure)

assertEqual :: (Eq a, Show a) => String -> a -> a -> IO ()
assertEqual label expected actual =
  unless (expected == actual) $ do
    putStrLn ("FAIL " ++ label ++ ": expected " ++ show expected ++ " got " ++ show actual)
    exitFailure

main :: IO ()
main = do
  assertEqual "example 1" "135" (digitSum "11111222223" 3)
  assertEqual "example 2" "000" (digitSum "00000000" 3)
  assertEqual "short string" "12" (digitSum "12" 3)
  putStrLn "practice1 digitSum: all cases passed"

