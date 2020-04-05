package br.ufrgs.rlnunes.tcc.leaderboard;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/leaderboard/admin")
public class LeaderboardAdminController {

    @GetMapping("/{leaderboardId}")
    public @ResponseBody String getTestData(@PathVariable String leaderboardId) {
        return leaderboardId;
    }

    @GetMapping("/")
    public @ResponseBody String test() {
        return "Pepino";
    }

    public LeaderboardAdminController() {
        System.out.println("OI");
    }
}