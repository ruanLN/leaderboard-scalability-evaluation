package br.ufrgs.rlnunes.tcc.leaderboard;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.mockito.ArgumentMatchers.any;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.MockitoAnnotations;

public class LeaderboardAdminServiceTest {

    LeaderboardAdminService leaderboardAdminService;

    @Mock
    LeaderboardRepository leaderboardRepository;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.initMocks(this);
        leaderboardAdminService = new LeaderboardAdminService(leaderboardRepository);
    }

    @Test
    void testCreateLeaderboard() {
        Mockito.when(leaderboardRepository.save(any(Leaderboard.class)))
            .thenReturn(new Leaderboard().withId(1L).withStatus(LeaderboardStatus.NOT_STARTED));
        Long leaderboardId = leaderboardAdminService.createLeaderboard();
        assertNotNull(leaderboardId);
        assertEquals(1L, leaderboardId);
        Mockito.verify(leaderboardRepository).save(any());
    }
}