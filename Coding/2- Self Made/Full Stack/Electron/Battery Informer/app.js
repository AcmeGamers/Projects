const {
  app,
  BrowserWindow,
  Menu,
  globalShortcut,
  Tray,
  ipcMain,
  Notification,
} = require("electron");
const AutoLaunch = require("auto-launch");
process.env.NODE_ENV = "production"; //development
const isDev = process.env.NODE_ENV !== "production" ? true : false,
  isMac = process.env.NODE_ENV === "darwin" ? true : false,
  isWin = process.env.NODE_ENV === "win32" ? true : false,
  isLin = process.env.NODE_ENV === "linux" ? true : false;

console.log(process.platform);

//////////////////////
// Application Windows
//////////////////////

// Assignments
let mainWindow, aboutWindow, notificationWindow, settingsWindow;

////////////////////////
/// Application Page ///
////////////////////////
const icon = __dirname + "\\assets\\battery-2.ico";

// Main Application
function runApplication() {
  mainWindow = new BrowserWindow({
    icon: icon,
    title: "Battery Informer",
    height: 400,
    width: 400,

    resizable: false,
    frame: false,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
    },
  });
  mainWindow.center();
  // isDev ? mainWindow.webContents.openDevTools() : null;
  mainWindow.loadFile("./app/start.html");

  // Hiding the Main Window
  mainWindow.on("close", (event) => {
    if (app.quitting) {
      mainWindow = null;
    } else {
      event.preventDefault();
      mainWindow.hide();
    }
  });
}

//////////////////
/// About Page ///
//////////////////
function aboutPage() {
  aboutWindow = new BrowserWindow({
    title: "About Battery Informer",
    icon: icon,
    width: 350,
    height: 400,
    resizable: false,
  });
  aboutWindow.loadFile("./app/about.html");
}

/////////////////////////
/// Notification Page ///
/////////////////////////

function notificationPage() {
  notificationWindow = new BrowserWindow({
    title: "Notification Page",
    icon: icon,
    height: 189,
    width: 428,
    resizable: false,
    frame: false,
  });
  notificationWindow.center();
  notificationWindow.loadFile("./app/notification.html");
}

/////////////////////
/// Settings Page ///
/////////////////////
function settingsPage() {
  settingsWindow = new BrowserWindow({
    title: "Settings",
    icon: icon,
    height: 230,
    width: 400,
    resizable: false,
    frame: false,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      // preload: "./preload.js",
    },
  });
  settingsWindow.center();
  settingsWindow.loadFile("./app/settings.html");
}

// Notification Alert On StartUp
app.setAppUserModelId("Battery Notifier");
const NOTIFICATION_TITLE = "Battery Notifier Active";
const NOTIFICATION_BODY = "Application is now active in the background.";

function showNotification() {
  new Notification({
    title: NOTIFICATION_TITLE,
    body: NOTIFICATION_BODY,
  }).show();
}

///////////////////////
// Starting Application
///////////////////////

app.on("ready", () => {
  runApplication();
  showNotification();
  // The Menu to be Made
  const mainmenu = Menu.buildFromTemplate(menu);

  // The Menu to Set
  Menu.setApplicationMenu(mainmenu);

  // Quit Menu
  // globalShortcut.register("CmdOrCtrl+W", () => app.quit());

  mainWindow.on("ready", () => (mainWindow = null));

  // Auto-Launch
  let autoLaunch = new AutoLaunch({
    name: "Battery Informer",
    path: app.getPath("exe"),
  });
  autoLaunch.isEnabled().then((isEnabled) => {
    if (!isEnabled) autoLaunch.enable();
  });
});

///////////////////
// Application Menu
///////////////////

const menu = [
  // About Page

  // Macintosh
  ...(isMac
    ? [
        { role: "appMenu" },
        {
          label: "File",
          submenu: [
            { label: "About " + app.name, click: () => aboutPage() },
            { type: "separator" },
            { label: "Settings", click: () => settingsPage() },
          ],
        },
      ]
    : [
        // Windows
        {
          label: "File",
          submenu: [
            {
              label: "Quit Appication",
              accelerator: "CmdOrCtrl+W",
              click: () => {
                app.quit();
              },
            },
          ],
          // role:"fileMenu"
        },
        {
          label: "Info",
          submenu: [
            { label: "About Battery Informer", click: () => aboutPage() },
            { type: "separator" },
            { label: "Settings", click: () => settingsPage() },
          ],
        },
      ]),

  ...(isDev
    ? [
        {
          label: "Developer Tools",
          submenu: [
            { label: "Notification Page", click: () => notificationPage() },
            { role: "reload" },
            { role: "forcereload" },
            { type: "separator" }, // Making a line in the menu
            { role: "toggledevtools" },
          ],
        },
      ]
    : []),
];

// Application Tray Icon

let tray = null;
app.whenReady().then(() => {
  tray = new Tray(icon);
  const contextMenu = Menu.buildFromTemplate([
    { label: "About", click: () => aboutPage() },
    { label: "Settings", click: () => settingsPage() },
    { type: "separator" },
    {
      label: "Exit",
      click: () => {
        app.exit();
      },
    },
  ]);
  tray.setToolTip("Battery Informer");
  tray.setContextMenu(contextMenu);
});

///////////////////////
// Battery Main Process
///////////////////////
const batteryLevel = require("battery-level");
batteryLevel().then((level) => {
  var totalBattery = level * 100;

  console.log(totalBattery);

  setInterval(function () {
    //this code runs every second

    if (totalBattery >= 60) {
      notificationPage();
    }
  }, 420000); // 7mins
  // 5000 5secs
  // 420000 7min
  // 1200000 20mins
});

ipcMain.on("form:value", (e, options) => {
  console.log(options.sliderValue);
});
