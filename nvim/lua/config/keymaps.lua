-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

function _G.set_terminal_keymaps()
  local opts = { buffer = 0 }
  vim.keymap.set("t", "<esc>", [[<Cmd>ToggleTerm<CR>]], opts)
  vim.keymap.set("t", "<C-h>", [[<Cmd>wincmd h<CR>]], opts)
  vim.keymap.set("t", "<C-j>", [[<Cmd>wincmd j<CR>]], opts)
  vim.keymap.set("t", "<C-k>", [[<Cmd>wincmd k<CR>]], opts)
  vim.keymap.set("t", "<C-l>", [[<Cmd>wincmd l<CR>]], opts)
  vim.keymap.set("t", "<C-w>", [[<Cmd>ToggleTerm<CR>]], opts)
end

-- if you only want these mappings for toggle term use term://*toggleterm#* instead
vim.cmd("autocmd! TermOpen term://*toggleterm#* lua set_terminal_keymaps()")
for i = 1, 5, 1 do
  vim.keymap.set(
    { "n", "t" },
    string.format("<A-%s>", i),
    string.format("<cmd>%sToggleTerm<cr>", i),
    { desc = "Open terminal" }
  )
end

-- Debugger
local dap = require("dap")
vim.keymap.set("n", "<leader>d<space>", dap.continue, { desc = "Continue" })
-- vim.keymap.set("n", "<leader>dj", dap.step_over, { desc = "Step over" })
-- vim.keymap.set("n", "<leader>dl", dap.step_into, { desc = "Step into" })
-- vim.keymap.set("n", "<leader>dh", dap.step_out, { desc = "Step out" })
-- vim.keymap.set("n", "<Leader>db", dap.toggle_breakpoint, { desc = "Toggle breakpoints" })
-- vim.keymap.set("n", "<Leader>dl", function()
--   dap.set_breakpoint(nil, nil, vim.fn.input("Log point message: "))
-- end, { desc = "Set logpoint" })
--
vim.keymap.set("n", "<leader>dm", require("dap-python").test_method, { desc = "Debug test method" })
vim.keymap.set("n", "<leader>dc", require("dap-python").test_class, { desc = "Debug test class" })
vim.keymap.set("n", "<leader>dt", function()
  require("neotest").run.run({ strategy = "dap" })
end, { desc = "Debug nearest test" })
vim.keymap.set("n", "<leader>dT", require("neotest").summary.toggle, { desc = "Toggle test summary" })

-- Resize terminal
vim.keymap.set("t", "<A-k>", "<cmd>resize +2<cr>", { desc = "Increase window height" })
vim.keymap.set("t", "<A-j>", "<cmd>resize -2<cr>", { desc = "Decrease window height" })

-- Resize window
vim.keymap.set("n", "<SA-h>", "<cmd>vertical resize +2<cr>", { desc = "Increase window width" })
vim.keymap.set("n", "<SA-l>", "<cmd>vertical resize -2<cr>", { desc = "Decrease window width" })
vim.keymap.set("n", "<SA-j>", "<cmd>resize +2<cr>", { desc = "Increase window height" })
vim.keymap.set("n", "<SA-k>", "<cmd>resize -2<cr>", { desc = "Decrease window height" })

vim.keymap.set({ "n", "i", "v" }, "<C-w>", function()
  require("mini.bufremove").delete(0, false)
end, { desc = "Delete Buffer" })
