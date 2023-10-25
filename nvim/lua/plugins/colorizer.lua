return {
  {
    "brenoprata10/nvim-highlight-colors",
    config = function(_, opts)
      require("nvim-highlight-colors").setup({
        render = "background", -- or 'foreground' or 'first_column'
        enable_named_colors = true,
        enable_tailwind = false,
      })
    end,
  },
}
