# Dungeondice-matrix

This is a quick re-make of [my discord dice-rolling bot](https://github.com/jwizzle/dungeondice).
For now quite barebones. It rolls dice. The code has been hastily copy/pasted.
Might make it prettier later.

## Features

- Roll dice in a matrix channel
- Roll multiple sets in one go `2x2d20`
- Add hints to your dice `d10(piercing)+d8(poison)`
- Add hints to your complete roll `d8(poison) For damage`
- Create complex rolls like `2x2d20(poison)+d8(piercing)-4` to get two total results

```
---------------------------------
2d20(poison)+d8(piercing)-4
Total: 35
Details: [[16, 17]33poison, [6]6piercing, [4]4]
---------------------------------
---------------------------------
2d20(poison)+d8(piercing)-4
Total: 19
Details: [[10, 11]21poison, [2]2piercing, [4]4]
---------------------------------
```

## Usage

```
MATRIX_HOST="https://your.host" BOT_USERNAME="@diceparser:your.host" BOT_PASSWORD="secret" uv run main.py
```
