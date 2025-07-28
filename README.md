# HALPI2 Documentation

This repository contains the HALPI2 User Guide source.

The documentation is written in Markdown format and is built using the Rust
`mdbook` tool. The output is a static website that can be hosted on any web server
(in our case, GitHub Pages).

The `mdBook` documentation can be found at [https://rust-lang.github.io/mdBook/](https://rust-lang.github.io/mdBook/).
To build the documentation locally, you need to have Rust and Cargo installed
as prerequisites. With them in place, you can install `mdBook` using:

```bash
cargo install mdbook
```

To build the documentation, run:

```bash
mdbook build
```

When writing documentation, you can preview it locally by running:

```bash
mdbook serve --open
```
This command will start a local server and open the documentation in your web browser.
