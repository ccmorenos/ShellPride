current_shell := $(shell echo $$SHELL)
current_shell_rc ?= ~/.$(shell echo $$SHELL | awk -F "/" '{print $$3}')rc

install-user:
	@echo "Installing scripts"

	@mkdir -p ~/.local/bin

	@cp -u shell/combinations/transbipride ~/.local/bin
	@cp -u shell/combinations/transgaypride ~/.local/bin
	@cp -u shell/combinations/translesbianpride ~/.local/bin
	@cp -u shell/combinations/translesbianpride2 ~/.local/bin
	@cp -u shell/gender/genderfluidpride ~/.local/bin
	@cp -u shell/gender/nonbinarypride ~/.local/bin
	@cp -u shell/gender/transpride ~/.local/bin
	@cp -u shell/gender/transpride2 ~/.local/bin
	@cp -u shell/gender/transpride3 ~/.local/bin
	@cp -u shell/gender/transpride4 ~/.local/bin
	@cp -u shell/pride ~/.local/bin
	@cp -u shell/progresspride ~/.local/bin
	@cp -u shell/sexuality/bipride ~/.local/bin
	@cp -u shell/sexuality/gaypride ~/.local/bin
	@cp -u shell/sexuality/gaypride2 ~/.local/bin
	@cp -u shell/sexuality/lesbianpride ~/.local/bin
	@cp -u shell/sexuality/lesbianpride2 ~/.local/bin

	@cp -u shell/pridelist ~/.local/bin

	@echo "Configuring resources file for $(current_shell)"
	@echo "export PATH=\$$PATH:~/.local/bin" >> $(current_shell_rc)

	@pride

install:
	@cp -u shell/combinations/transbipride /usr/bin
	@cp -u shell/combinations/transgaypride /usr/bin
	@cp -u shell/combinations/translesbianpride /usr/bin
	@cp -u shell/combinations/translesbianpride2 /usr/bin
	@cp -u shell/gender/genderfluidpride /usr/bin
	@cp -u shell/gender/nonbinarypride /usr/bin
	@cp -u shell/gender/transpride /usr/bin
	@cp -u shell/gender/transpride2 /usr/bin
	@cp -u shell/gender/transpride3 /usr/bin
	@cp -u shell/gender/transpride4 /usr/bin
	@cp -u shell/pride /usr/bin
	@cp -u shell/progresspride /usr/bin
	@cp -u shell/sexuality/bipride /usr/bin
	@cp -u shell/sexuality/gaypride /usr/bin
	@cp -u shell/sexuality/gaypride2 /usr/bin
	@cp -u shell/sexuality/lesbianpride /usr/bin
	@cp -u shell/sexuality/lesbianpride2 /usr/bin

	@cp -u shell/pridelist /usr/bin

	@pride

uninstall:
	@rm -f /usr/bin/transbipride
	@rm -f /usr/bin/transgaypride
	@rm -f /usr/bin/translesbianpride
	@rm -f /usr/bin/translesbianpride2
	@rm -f /usr/bin/genderfluidpride
	@rm -f /usr/bin/nonbinarypride
	@rm -f /usr/bin/transpride
	@rm -f /usr/bin/transpride2
	@rm -f /usr/bin/transpride3
	@rm -f /usr/bin/transpride4
	@rm -f /usr/bin/pride
	@rm -f /usr/bin/progresspride
	@rm -f /usr/bin/bipride
	@rm -f /usr/bin/gaypride
	@rm -f /usr/bin/gaypride2
	@rm -f /usr/bin/lesbianpride
	@rm -f /usr/bin/lesbianpride2

	@rm -f /usr/bin/pridelist
