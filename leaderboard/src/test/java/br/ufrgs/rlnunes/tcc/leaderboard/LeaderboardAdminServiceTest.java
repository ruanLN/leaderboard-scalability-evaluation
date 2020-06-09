package br.ufrgs.rlnunes.tcc.leaderboard;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.mockito.ArgumentMatchers.any;

import java.util.Optional;

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
                .thenReturn(Leaderboard.builder().id(1L).status(LeaderboardStatus.NOT_STARTED).build());
        Long leaderboardId = leaderboardAdminService.createLeaderboard();
        assertNotNull(leaderboardId);
        assertEquals(1L, leaderboardId);
        Mockito.verify(leaderboardRepository).save(any());
    }

    @Test
    void testGetLeaderboard() {
        Mockito.when(leaderboardRepository.findById(1L))
                .thenReturn(Optional.of(Leaderboard.builder().id(1L).status(LeaderboardStatus.NOT_STARTED).build()));
        Optional<Leaderboard> leaderboard = leaderboardAdminService.getLeaderboard(1L);
        assertEquals(Optional.of(Leaderboard.builder().id(1L).status(LeaderboardStatus.NOT_STARTED).build()), leaderboard);
    }
}