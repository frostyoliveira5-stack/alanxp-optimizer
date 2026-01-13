import tkinter as tk
from tkinter import messagebox
import subprocess
import ctypes
import sys

class AlanXPOptimizer:
    def __init__(self, root):
        self.root = root
        self.root.title("AlanXP Optimizer V1")
        self.root.geometry("700x550")
        self.root.configure(bg='#1a1a1a')
        self.root.resizable(False, False)
        
        # Verificar privilégios de administrador
        if not self.is_admin():
            messagebox.showwarning("Aviso", "Execute como Administrador para funcionalidade completa!")
        
        # Estados dos toggles
        self.toggles = {}
        
        self.create_ui()
    
    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    
    def create_ui(self):
        # Header
        header_frame = tk.Frame(self.root, bg='#0d0d0d', height=80)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text="AlanXP Optimizer", 
                              font=('Arial', 24, 'bold'), 
                              fg='#ff3333', bg='#0d0d0d')
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(header_frame, text="Otimização Avançada para Windows", 
                                 font=('Arial', 10), 
                                 fg='#cccccc', bg='#0d0d0d')
        subtitle_label.pack()
        
        # Container principal
        main_frame = tk.Frame(self.root, bg='#1a1a1a')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Configurações de otimização
        optimizations = [
            ("Desativar Telemetria", self.disable_telemetry),
            ("Otimizar Serviços", self.optimize_services),
            ("Limpar Temp", self.clean_temp),
            ("Desativar Efeitos Visuais", self.disable_visual_effects),
            ("Otimizar Energia", self.optimize_power),
            ("Desativar Cortana", self.disable_cortana),
            ("Otimizar Rede", self.optimize_network),
            ("Desativar Xbox", self.disable_xbox),
            ("Prioridade GPU", self.gpu_priority),
            ("Desativar Rastreamento", self.disable_tracking),
            ("Otimizar SSD", self.optimize_ssd),
            ("Limpar Prefetch", self.clean_prefetch),
            ("Desativar Hibernação", self.disable_hibernation),
            ("Otimizar Registro", self.optimize_registry),
            ("Modo Alto Desempenho", self.high_performance_mode),
        ]
        
        # Criar grid de botões
        row = 0
        col = 0
        for i, (name, func) in enumerate(optimizations):
            self.create_toggle_button(main_frame, name, func, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1
        
        # Botão de aplicar todas as otimizações
        apply_frame = tk.Frame(self.root, bg='#1a1a1a')
        apply_frame.pack(fill='x', padx=20, pady=10)
        
        apply_btn = tk.Button(apply_frame, text="🚀 APLICAR TODAS OTIMIZAÇÕES", 
                             font=('Arial', 12, 'bold'),
                             bg='#ff3333', fg='white',
                             activebackground='#cc0000',
                             relief='flat',
                             cursor='hand2',
                             command=self.apply_all,
                             height=2)
        apply_btn.pack(fill='x')
        
        # Footer
        footer_label = tk.Label(self.root, text="© 2025 AlanXP - Todos os direitos reservados", 
                               font=('Arial', 8), 
                               fg='#666666', bg='#1a1a1a')
        footer_label.pack(pady=5)
    
    def create_toggle_button(self, parent, text, command, row, col):
        frame = tk.Frame(parent, bg='#2a2a2a', relief='solid', borderwidth=1)
        frame.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
        
        parent.grid_rowconfigure(row, weight=1)
        parent.grid_columnconfigure(col, weight=1)
        
        self.toggles[text] = False
        
        def toggle():
            self.toggles[text] = not self.toggles[text]
            if self.toggles[text]:
                btn.config(bg='#ff3333', activebackground='#cc0000')
                command()
            else:
                btn.config(bg='#444444', activebackground='#555555')
        
        btn = tk.Button(frame, text=text, 
                       font=('Arial', 9, 'bold'),
                       bg='#444444', fg='white',
                       activebackground='#555555',
                       relief='flat',
                       cursor='hand2',
                       command=toggle,
                       wraplength=150,
                       height=3)
        btn.pack(fill='both', expand=True, padx=2, pady=2)
    
    def run_command(self, command, shell=True):
        try:
            result = subprocess.run(command, shell=shell, capture_output=True, text=True)
            return result.returncode == 0
        except Exception as e:
            print(f"Erro: {e}")
            return False
    
    def disable_telemetry(self):
        commands = [
            'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection" /v AllowTelemetry /t REG_DWORD /d 0 /f',
            'sc config DiagTrack start= disabled',
            'sc stop DiagTrack'
        ]
        for cmd in commands:
            self.run_command(cmd)
        messagebox.showinfo("Sucesso", "Telemetria desativada!")
    
    def optimize_services(self):
        services = ['SysMain', 'WSearch', 'RetailDemo', 'TabletInputService']
        for service in services:
            self.run_command(f'sc config {service} start= disabled')
            self.run_command(f'sc stop {service}')
        messagebox.showinfo("Sucesso", "Serviços otimizados!")
    
    def clean_temp(self):
        commands = [
            'del /q/f/s %TEMP%\\* 2>nul',
            'del /q/f/s C:\\Windows\\Temp\\* 2>nul',
            'cleanmgr /sagerun:1'
        ]
        for cmd in commands:
            self.run_command(cmd)
        messagebox.showinfo("Sucesso", "Arquivos temporários limpos!")
    
    def disable_visual_effects(self):
        cmd = 'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects" /v VisualFXSetting /t REG_DWORD /d 2 /f'
        self.run_command(cmd)
        messagebox.showinfo("Sucesso", "Efeitos visuais desativados!")
    
    def optimize_power(self):
        self.run_command('powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61')
        self.run_command('powercfg -setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c')
        messagebox.showinfo("Sucesso", "Energia otimizada!")
    
    def disable_cortana(self):
        cmd = 'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search" /v AllowCortana /t REG_DWORD /d 0 /f'
        self.run_command(cmd)
        messagebox.showinfo("Sucesso", "Cortana desativada!")
    
    def optimize_network(self):
        commands = [
            'netsh int tcp set global autotuninglevel=normal',
            'netsh int tcp set global chimney=enabled',
            'netsh int tcp set global dca=enabled',
            'netsh int tcp set global netdma=enabled'
        ]
        for cmd in commands:
            self.run_command(cmd)
        messagebox.showinfo("Sucesso", "Rede otimizada!")
    
    def disable_xbox(self):
        services = ['XblAuthManager', 'XblGameSave', 'XboxNetApiSvc', 'XboxGipSvc']
        for service in services:
            self.run_command(f'sc config {service} start= disabled')
            self.run_command(f'sc stop {service}')
        messagebox.showinfo("Sucesso", "Xbox desativado!")
    
    def gpu_priority(self):
        cmd = 'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games" /v "GPU Priority" /t REG_DWORD /d 8 /f'
        self.run_command(cmd)
        messagebox.showinfo("Sucesso", "Prioridade GPU configurada!")
    
    def disable_tracking(self):
        commands = [
            'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\AppPrivacy" /v LetAppsAccessLocation /t REG_DWORD /d 2 /f',
            'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Privacy" /v TailoredExperiencesWithDiagnosticDataEnabled /t REG_DWORD /d 0 /f'
        ]
        for cmd in commands:
            self.run_command(cmd)
        messagebox.showinfo("Sucesso", "Rastreamento desativado!")
    
    def optimize_ssd(self):
        self.run_command('fsutil behavior set DisableDeleteNotify 0')
        messagebox.showinfo("Sucesso", "SSD otimizado!")
    
    def clean_prefetch(self):
        self.run_command('del /q/f/s C:\\Windows\\Prefetch\\* 2>nul')
        messagebox.showinfo("Sucesso", "Prefetch limpo!")
    
    def disable_hibernation(self):
        self.run_command('powercfg -h off')
        messagebox.showinfo("Sucesso", "Hibernação desativada!")
    
    def optimize_registry(self):
        commands = [
            'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v ClearPageFileAtShutdown /t REG_DWORD /d 0 /f',
            'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v DisablePagingExecutive /t REG_DWORD /d 1 /f'
        ]
        for cmd in commands:
            self.run_command(cmd)
        messagebox.showinfo("Sucesso", "Registro otimizado!")
    
    def high_performance_mode(self):
        self.run_command('powercfg -setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c')
        messagebox.showinfo("Sucesso", "Modo alto desempenho ativado!")
    
    def apply_all(self):
        if messagebox.askyesno("Confirmar", "Aplicar todas as otimizações?\n\nÉ recomendado criar um ponto de restauração antes."):
            self.disable_telemetry()
            self.optimize_services()
            self.clean_temp()
            self.disable_visual_effects()
            self.optimize_power()
            self.disable_cortana()
            self.optimize_network()
            self.disable_xbox()
            self.gpu_priority()
            self.disable_tracking()
            self.optimize_ssd()
            self.clean_prefetch()
            self.disable_hibernation()
            self.optimize_registry()
            self.high_performance_mode()
            messagebox.showinfo("Concluído", "Todas as otimizações foram aplicadas!\n\nReinicie o computador para aplicar todas as mudanças.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AlanXPOptimizer(root)
    root.mainloop()
