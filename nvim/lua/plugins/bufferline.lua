return {
  "akinsho/bufferline.nvim",
  event = "VeryLazy",
  keys = {
    { "<leader>bp", "<Cmd>BufferLineTogglePin<CR>", desc = "Toggle Pin" },
    { "<leader>bP", "<Cmd>BufferLineGroupClose ungrouped<CR>", desc = "Delete Non-Pinned Buffers" },
    { "<leader>bo", "<Cmd>BufferLineCloseOthers<CR>", desc = "Delete Other Buffers" },
    { "<leader>br", "<Cmd>BufferLineCloseRight<CR>", desc = "Delete Buffers to the Right" },
    { "<leader>bl", "<Cmd>BufferLineCloseLeft<CR>", desc = "Delete Buffers to the Left" },
    { "<S-h>", "<cmd>BufferLineCyclePrev<cr>", desc = "Prev Buffer" },
    { "<S-l>", "<cmd>BufferLineCycleNext<cr>", desc = "Next Buffer" },
    { "[b", "<cmd>BufferLineCyclePrev<cr>", desc = "Prev Buffer" },
    { "]b", "<cmd>BufferLineCycleNext<cr>", desc = "Next Buffer" },
  },
  opts = {
    options = {
      middle_mouse_command = function(n)
        require("mini.bufremove").delete(n, false)
      end,
      indicator = { style = "none" },
      diagnostics = "nvim_lsp",
      always_show_bufferline = true,
      diagnostics_indicator = function(count, level, diag, context)
        local icons = require("lazyvim.config").icons.diagnostics
        local ret = (diag.error and icons.Error .. diag.error .. " " or "")
          .. (diag.warning and icons.Warn .. diag.warning .. " " or "")
          .. (diag.info and icons.Info .. diag.info .. " " or "")
          .. (diag.hint and icons.Hint .. diag.hint .. " " or "")
        return vim.trim(ret)
      end,
      offsets = {
        {
          filetype = "neo-tree",
          text = "Neo-tree",
          highlight = "Directory",
          text_align = "left",
        },
      },
      color_icons = false,
      show_buffer_icons = true,
      show_buffer_close_icons = false,
      show_tab_indicators = false,
      separator_style = { "", "" },
    },
  },
  config = function(_, opts)
    local bl = require("bufferline")
    local colors = require("kanagawa.colors").setup()
    local palette_colors = colors.palette
    local theme_colors = colors.theme

    opts.options.style_preset = bl.style_preset.minimal
    opts.highlights = {
      buffer_selected = {
        bg = palette_colors.autumnGreen,
        fg = palette_colors.sumiInk0,
        bold = true,
        italic = false,
      },
      hint_selected = {
        bg = palette_colors.autumnGreen,
        fg = palette_colors.sumiInk0,
        bold = true,
        italic = false,
      },
      hint_diagnostic = {
        fg = theme_colors.diag.hint,
        bold = true,
        italic = false,
      },
      hint_diagnostic_selected = {
        bg = palette_colors.autumnGreen,
        fg = palette_colors.sumiInk0,
        bold = true,
        italic = false,
      },
      info_selected = {
        bg = palette_colors.autumnGreen,
        fg = palette_colors.sumiInk0,
        bold = true,
        italic = false,
      },
      info_diagnostic = {
        fg = theme_colors.diag.info,
        bold = true,
        italic = false,
      },
      info_diagnostic_selected = {
        bg = palette_colors.autumnGreen,
        fg = palette_colors.sumiInk0,
        bold = true,
        italic = false,
      },
      warning_diagnostic = {
        fg = theme_colors.diag.warning,
        bold = true,
        italic = false,
      },
      warning_selected = {
        bg = palette_colors.autumnGreen,
        fg = palette_colors.sumiInk0,
        bold = true,
        italic = false,
      },
      warning_diagnostic_selected = {
        bg = palette_colors.autumnGreen,
        fg = palette_colors.sumiInk0,
        bold = true,
        italic = false,
      },
      error_diagnostic = {
        fg = theme_colors.diag.error,
        bold = true,
        italic = false,
      },
      error_selected = {
        bg = palette_colors.autumnGreen,
        fg = palette_colors.sumiInk0,
        bold = true,
        italic = false,
      },
      error_diagnostic_selected = {
        bg = palette_colors.autumnGreen,
        fg = palette_colors.sumiInk0,
        bold = true,
        italic = false,
      },
      indicator_selected = {
        bg = palette_colors.autumnGreen,
        fg = palette_colors.sumiInk0,
      },
      modified_selected = {
        bg = palette_colors.autumnGreen,
        fg = palette_colors.sumiInk0,
      },
      duplicate_selected = {
        bg = palette_colors.autumnGreen,
        fg = palette_colors.sumiInk0,
        italic = true,
      },
    }
    bl.setup(opts)
    -- Fix bufferline when restoring a session
    vim.api.nvim_create_autocmd("BufAdd", {
      callback = function()
        vim.schedule(function()
          pcall(nvim_bufferline)
        end)
      end,
    })
  end,
}
