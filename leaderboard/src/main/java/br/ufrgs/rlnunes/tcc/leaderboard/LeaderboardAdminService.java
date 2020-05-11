package br.ufrgs.rlnunes.tcc.leaderboard;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class LeaderboardAdminService {
    LeaderboardRepository leaderboardRepository;

    @Autowired
    public LeaderboardAdminService(LeaderboardRepository leaderboardRepository) {
        this.leaderboardRepository = leaderboardRepository;
    }

    public Long createLeaderboard() {
        Leaderboard savedEntity = leaderboardRepository.save(new Leaderboard(LeaderboardStatus.NOT_STARTED));
        return savedEntity.getId();
    }

    public void destroyLeaderboard(Long leaderboardId) {
        
    }

    public void enableLeaderboard(Long leaderboardId) {
        
    }

    public void disableLeaderboard(Long leaderboardId) {

    }
}