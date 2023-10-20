return {
  { "catppuccin/nvim" },
  {
    "rebelot/kanagawa.nvim",
    opts = {
      transparent = true,
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
    "folke/tokyonight.nvim",
    opts = {
      transparent = true,
      styles = {
        sidebars = "transparent",
        floats = "transparent",
      },
    },
  },
  -- {
  --   "LazyVim/LazyVim",
  --   opts = {
  --     colorscheme = "tokyonight",
  --   },
  -- },
}
