return {
  { "catppuccin/nvim" },
  {
    "rebelot/kanagawa.nvim",
    opts = {
      transparent = false,
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
  -- {
  --   "folke/tokyonight.nvim",
  --   opts = {
  --     transparent = false,
  --   },
  -- },
}
