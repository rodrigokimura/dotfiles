return {
  { "catppuccin/nvim", enabled = false },
  {
    "rebelot/kanagawa.nvim",
    opts = {
      commentstyle = { italic = true },
      overrides = function(colors)
        return {
          TabLineSel = { bg = colors.palette.surimiOrange },
        }
      end,
    },
    config = function(_, opts)
      local kanagawa = require("kanagawa")
      kanagawa.setup(opts)
      kanagawa.load("wave")
    end,
  },
  {
    "LazyVim/LazyVim",
    colorscheme = "kanagawa",
  },
}
