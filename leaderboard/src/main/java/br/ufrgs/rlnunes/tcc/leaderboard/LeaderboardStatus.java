package br.ufrgs.rlnunes.tcc.leaderboard;

public enum LeaderboardStatus {
    NOT_STARTED(0),
    STARTED(1),
    FINISHED(2);

    public int status;

    LeaderboardStatus(int status) {
        this.status = status;
    }
}