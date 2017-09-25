#pragma once

#define GLFW_INCLUDE_GLU

#include <GLFW/glfw3.h>
#include "imgui.h"
#include <string>
#include <functional>
#include "rendering.h"

namespace rs2
{
    class viewer_ui_traits
    {
    public:
        const static int control_panel_width = 280;
        const static int control_panel_height = 40;
        const static int metrics_panel_width = 250;
        const static int default_log_h = 80;
        // Flags for pop-up window - no window resize, move or collaps
        const static auto imgui_flags = ImGuiWindowFlags_NoResize | ImGuiWindowFlags_NoMove |
            ImGuiWindowFlags_NoCollapse | ImGuiWindowFlags_NoTitleBar |
            ImGuiWindowFlags_NoSavedSettings;
    };

    class ux_window
    {
    public:
        std::function<void(std::string)> on_file_drop = [](std::string) {};
        std::function<void()>            on_load = [](){};

        ux_window(const char* title);

        float width() const { return float(_width); }
        float height() const { return float(_height); }

        // Check that the graphic subsystem is valid and start a new frame
        operator bool();

        ~ux_window();

        operator GLFWwindow*() { return _win; }

        void begin_frame();

        void begin_viewport();

        void end_frame();

        ImFont* get_large_font() const { return _font_18; }
        ImFont* get_font() const { return _font_14; }

        rs2::mouse_info& get_mouse() { return _mouse; }
        float get_scale_factor() const { return _scale_factor; }

    private:
        ux_window(const ux_window&);

        GLFWwindow              *_win;
        int                     _width, _height, _output_height;
        rs2::rect               _viewer_rect;

        ImFont                  *_font_14, *_font_18;
        rs2::mouse_info         _mouse;
        std::string             _error_message;
        float                   _scale_factor;

        bool                    _first_frame = true;
        std::atomic<bool>       _app_ready;
        texture_buffer          _splash_tex;
        timer                   _splash_timer;
        std::string             _title_str;
    };
}