import i3ipc

def adjust_layout(sway, event):
    # Get the container/workspace where the event happened
    con = event.container
    workspace = con.workspace()
    
    # Count tiled (non-floating) windows in that workspace
    tiled_windows = [leaf for leaf in workspace.leaves() if leaf.type == 'con' and not leaf.floating]
    
    # Logic: >1 window = tabbed, 1 window = default (splith/splitv)
    if len(tiled_windows) > 1:
        workspace.command('layout tabbed')
    elif len(tiled_windows) == 1:
        workspace.command('layout default')

sway = i3ipc.Connection()

# Listen for new windows, closed windows, and windows moved between workspaces
sway.on('window::new', adjust_layout)
sway.on('window::close', adjust_layout)
sway.on('window::move', adjust_layout)

sway.main()
