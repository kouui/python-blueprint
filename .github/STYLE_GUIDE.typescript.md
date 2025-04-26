# Coding Style Guide

This document outlines coding standards for our project.

## TypeScript

### Formatting
- **Consistency is Key:** Use a formatter like Prettier! Configure it project-wide to handle most of this automatically.
- **Indentation:** Use 2 spaces for indentation (common TS convention, but configure via Prettier).
- **Line Length:** Aim for a maximum line length of 100-120 characters (configurable via Prettier).
- **Semicolons:** Use semicolons `;` at the end of statements (enforced by Prettier).
- **Trailing Commas:** Use trailing commas in multi-line arrays, objects, and type/interface definitions (helps with Git diffs, configure via Prettier).

### Naming
- Variables and functions: `camelCase` (like a bumpy camel ride).
- Classes, Interfaces, Types, Enums: `PascalCase` (standing tall, again!).
- Constants: `UPPER_SNAKE_CASE` for true constants (global/static values that never change). Use `camelCase` for `const` variables that aren't globally constant.
- Private members: Use the `private` keyword. Consider `#privateField` syntax for ECMAScript private fields where appropriate. Avoid underscore (`_`) prefixes for privacy.

### Strings
- **Quotes:** Prefer single quotes (`'`) for string literals (often default in Prettier configs for TS/JS).
- **Interpolation & Multi-line:** Use template literals (backticks `` ` ``) for string interpolation (`Hello ${name}!`) and multi-line strings.

### Comments & Documentation
- **JSDoc:** Use `/** JSDoc comments */` for documenting functions, classes, interfaces, types, and complex logic. Explain purpose, parameters (`@param`), return values (`@returns`), etc. Copilot uses these!
- **Inline Comments:** Use `//` for single-line comments explaining non-obvious code or leaving short notes.
- **Block Comments:** Use `/* Block comments */` for longer explanations or temporarily commenting out code sections (though `//` per line is often clearer).

### Types (It's TypeScript, after all!)
- **Static Typing:** Leverage TypeScript's type system! Avoid `any` whenever possible.
- **Interfaces vs Types:** Prefer `interface` for defining the shape of objects or implementing classes. Use `type` for aliases, unions, intersections, conditional types, etc. (Establish a team convention if needed).
- **`Readonly`:** Use `readonly` for properties that should not be reassigned after object creation.
- **Enums:** Prefer string enums (`enum Color { Red = "RED" }`) over numeric enums unless you have a specific reason for numeric values.
- **Strict Checks:** Enable `strictNullChecks` and other `strict` compiler options in `tsconfig.json`.

### Error Handling
- Use `try...catch` blocks for synchronous code that might throw errors.
- Use `async/await` with `try...catch` for handling errors in asynchronous (Promise-based) code.
- Catch specific `Error` types or check error properties (`instanceof`, `error.code`) instead of generic `catch (e)`.
- Include logging for caught exceptions, providing useful context.

### Modules & Imports
- Use ES6 module syntax (`import`/`export`).
- Prefer named exports (`export const myVar; export function myFunc;`) over default exports (`export default ...`) for better discoverability and refactoring.
- Organize imports (often handled by linters/IDEs): standard libraries first, then third-party, then local modules.

### General Best Practices
- **`const` over `let`:** Prefer `const` for variable declarations unless the variable needs to be reassigned.
- **Arrow Functions:** Use arrow functions (`=>`) for callbacks and when preserving `this` context, but use traditional `function` syntax for class methods where appropriate.